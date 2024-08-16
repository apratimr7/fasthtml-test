import * as THREE from 'three';
// import { OrbitControls } from "three/addons/controls/OrbitControls.js";

// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({canvas: document.querySelector("#background-canvas"),
  antialias: true});
renderer.setSize(window.innerWidth, window.innerHeight);
// document.body.appendChild(renderer.domElement);

// const controls = new OrbitControls(camera, renderer.domElement);
// controls.enableDamping = true;
// controls.dampingFactor = 0.3;
// controls.enablePan = true;
// controls.enableZoom = true;

// Create a custom circular texture
function createParticleTexture() {
    const size = 128;
    const canvas = document.createElement('canvas');
    canvas.width = size;
    canvas.height = size;

    const ctx = canvas.getContext('2d');
    const gradient = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    
    // Create a gradient from white to transparent
    gradient.addColorStop(0, 'rgba(255, 255, 255, 1)');
    gradient.addColorStop(0.2, 'rgba(255, 255, 255, 0.8)');
    gradient.addColorStop(0.4, 'rgba(255, 255, 255, 0.6)');
    gradient.addColorStop(1, 'rgba(255, 255, 255, 0)');
    
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(size / 2, size / 2, size / 2, 0, Math.PI * 2, false);
    ctx.fill();

    const texture = new THREE.CanvasTexture(canvas);
    return texture;
}

// Particle system setup
const particles = new THREE.BufferGeometry();
const particleCount = 2000;

const positions = [];
const velocities = [];

for (let i = 0; i < particleCount; i++) {
    positions.push((Math.random() * 2 - 1) * 500);
    positions.push((Math.random() * 2 - 1) * 500);
    positions.push((Math.random() * 2 - 1) * 500);
    
    velocities.push((Math.random() - 0.5) * 0.1);
    velocities.push((Math.random() - 0.5) * 0.1);
    velocities.push((Math.random() - 0.5) * 0.1);
}

particles.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

const particleMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 3,
    map: createParticleTexture(),  // Use the generated texture
    blending: THREE.AdditiveBlending,
    transparent: true
});

const particleSystem = new THREE.Points(particles, particleMaterial);
scene.add(particleSystem);

camera.position.z = 500;

// Mouse tracking
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', function(event) {
    mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
});

function animate() {
    requestAnimationFrame(animate);

    // Move particles
    const positions = particles.attributes.position.array;
    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] += velocities[i * 3];
        positions[i * 3 + 1] += velocities[i * 3 + 1];
        positions[i * 3 + 2] += velocities[i * 3 + 2];

        if (positions[i * 3] > 500 || positions[i * 3] < -500) velocities[i * 3] *= -1;
        if (positions[i * 3 + 1] > 500 || positions[i * 3 + 1] < -500) velocities[i * 3 + 1] *= -1;
        if (positions[i * 3 + 2] > 500 || positions[i * 3 + 2] < -500) velocities[i * 3 + 2] *= -1;
    }
    particles.attributes.position.needsUpdate = true;

    // Update camera position to follow mouse
    camera.position.x += (mouseX * 100 - camera.position.x) * 0.05;
    camera.position.y += (mouseY * 100 - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
}

animate();

window.addEventListener('resize', onWindowResize, false);

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}