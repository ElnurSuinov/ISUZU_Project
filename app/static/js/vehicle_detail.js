import * as THREE from "https://esm.sh/three@0.160.0";
import { GLTFLoader } from "https://esm.sh/three@0.160.0/examples/jsm/loaders/GLTFLoader.js";
import { OrbitControls } from "https://esm.sh/three@0.160.0/examples/jsm/controls/OrbitControls.js";

/* ---- Scene setup ---- */
const canvas = document.getElementById('scene');
if (!canvas) throw new Error("Canvas #scene not found");

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(canvas.clientWidth, canvas.clientHeight);
renderer.setClearColor(0xcccccc);
renderer.outputEncoding = THREE.sRGBEncoding;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
const defaultPosition = new THREE.Vector3(0, 1.5, 3);
camera.position.copy(defaultPosition);

/* ---- Lights ---- */
const hemiLight = new THREE.HemisphereLight(0xffffff, 0x888888, 1.0);
hemiLight.position.set(0, 2, 0);
scene.add(hemiLight);
const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
dirLight.position.set(3, 5, 2);
scene.add(dirLight);

/* ---- Controls ---- */
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.target.set(0, 1, 0);
controls.update();

/* ---- Model Loader ---- */
let loadedModel = null;
const loader = new GLTFLoader();
const modelPath = `/static/3d/${canvas.dataset.model}`;

loader.load(modelPath, (gltf) => {
  loadedModel = gltf.scene;
  scene.add(loadedModel);
  fitCameraToObject(camera, loadedModel, controls);
  animate();
}, undefined, (error) => {
  console.error("Error loading model:", error);
});

/* ---- Helpers ---- */
function fitCameraToObject(camera, object, controls, offset = 1.5) {
  const box = new THREE.Box3().setFromObject(object);
  const size = box.getSize(new THREE.Vector3());
  const center = box.getCenter(new THREE.Vector3());
  const maxDim = Math.max(size.x, size.y, size.z);
  const fov = camera.fov * (Math.PI / 180);
  const cameraZ = Math.abs(maxDim / Math.sin(fov / 2)) * 0.5 * offset;
  camera.position.set(center.x, center.y + size.y * 0.3, cameraZ);
  controls.target.copy(center);
  controls.update();
}

/* ---- Reset View ---- */
document.getElementById('resetView').addEventListener('click', () => {
  const duration = 1000;
  const start = performance.now();
  const startPos = camera.position.clone();
  const startTarget = controls.target.clone();
  const endPos = defaultPosition.clone();
  const endTarget = new THREE.Vector3(0, 1, 0);

  function step(now) {
    const t = Math.min((now - start) / duration, 1);
    const ease = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    camera.position.lerpVectors(startPos, endPos, ease);
    controls.target.lerpVectors(startTarget, endTarget, ease);
    controls.update();
    if (t < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
});

/* ---- Dynamic Trim / Colors / Specs ---- */
const trimSelect = document.getElementById('trimSelect');
const colorOptions = document.getElementById('colorOptions');
const specsTable = document.getElementById('specsTable');

function renderColors(colors) {
  colorOptions.innerHTML = '';
  colors.forEach(color => {
    const btn = document.createElement('button');
    btn.classList.add('color-btn');
    btn.dataset.color = color;
    btn.style.backgroundColor = color;
    btn.addEventListener('click', () => changeModelColor(color, btn));
    colorOptions.appendChild(btn);
  });
}

function changeModelColor(newColorHex, btn) {
  const newColor = new THREE.Color(newColorHex);
  if (!loadedModel) return;
  const buttons = Array.from(document.querySelectorAll('.color-btn'));
  buttons.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  loadedModel.traverse((child) => {
    if (child.isMesh && child.material) {
      const startColor = child.material.color.clone();
      const start = performance.now();
      const duration = 800;
      function fade(now) {
        const t = Math.min((now - start) / duration, 1);
        child.material.color.lerpColors(startColor, newColor, t);
        if (t < 1) requestAnimationFrame(fade);
      }
      fade(performance.now());
    }
  });
}

function renderSpecs(specs) {
  specsTable.innerHTML = '';
  for (const [key, value] of Object.entries(specs)) {
    const row = document.createElement('tr');
    row.innerHTML = `<th>${key}</th><td>${value}</td>`;
    specsTable.appendChild(row);
  }
}

function updateTrimDisplay() {
  const option = trimSelect.selectedOptions[0];
  const specs = JSON.parse(option.dataset.specs);
  const colors = JSON.parse(option.dataset.colors);
  renderSpecs(specs);
  renderColors(colors);
}

// Initialize first trim
updateTrimDisplay();
trimSelect.addEventListener('change', updateTrimDisplay);

/* ---- Animate ---- */
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

/* ---- Responsive Resize ---- */
window.addEventListener('resize', () => {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);
});
