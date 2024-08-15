import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";


const w = window.innerWidth;
const h = window.innerHeight;
const renderer = new THREE.WebGLRenderer({ 
  canvas: document.querySelector("#background-canvas"),
  antialias: true});
renderer.setSize(w,h);
// document.body.appendChild(renderer.domElement);
const fov = 75; //field of view
const aspect = w/h;
const near = 0.1;
const far = 10;
const camera = new THREE.PerspectiveCamera(fov,aspect, near, far);
camera.position.z = 5;
const scene = new THREE.Scene();

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.03;

// Generate the spline data
const wormholeSplinePoints = generateWormholeSplineData();
// Create a SplineCurve object
const wormholeCurve = new THREE.CatmullRomCurve3(wormholeSplinePoints);

const points = wormholeCurve.getPoints(100)
const geometry = new THREE.BufferGeometry().setFromPoints(points);
const material = new THREE.LineBasicMaterial({
    color:0xff0000
});
const line = new THREE.Line(geometry,material);
// scene.add(line);

scene.fog = new THREE.FogExp2(0x000000,0.6);

// Create a TubeGeometry to visualize the spline
const tubeGeometry = new THREE.TubeGeometry(wormholeCurve, 222, 0.65, 16, false);
const tubeMaterial = new THREE.MeshBasicMaterial({ 
    color: 0xffffff, 
    side: THREE.DoubleSide,
    wireframe: true });
const tubeMesh = new THREE.Mesh(tubeGeometry, tubeMaterial);
// Add the wormhole to the scene
// scene.add(tubeMesh);

// CREATE EDGE GEOMETRY
const edges = new THREE.EdgesGeometry(tubeGeometry,0.2);
const lineMat = new THREE.LineBasicMaterial({color:0xffffff});
const tubeLines = new THREE.LineSegments(edges,lineMat);
scene.add(tubeLines)



function updateCamera(t){
     const time = t *0.1;
     const looptime = 8*1000;
     const p = (time%looptime)/looptime;
     const pos = tubeGeometry.parameters.path.getPointAt(p);
     const lookAt = tubeGeometry.parameters.path.getPointAt((p+0.03)%1);
     camera.position.copy(pos);
     camera.lookAt(lookAt);
}

function animate(t=0){
    requestAnimationFrame(animate);
    updateCamera(t);
    renderer.render(scene,camera);
    controls.update();
}
animate();

window.addEventListener('resize', onWindowResize, false);

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}


function generateWormholeSplineData(numPoints = 100, radius = 3, length = 50, twists = 6.5,randomFactor = 0.1) {
    const splinePoints = [];
    const frequency = twists * 2 * Math.PI / length;  // Frequency of twists
    const amplitudeX = radius;  // Amplitude of displacement in the x direction
    const amplitudeY = radius * 0.5;  // Amplitude of displacement in the y direction (slightly smaller for variety)
    
    let randomSeedX = Math.random() * 100;
    let randomSeedY = Math.random() * 100;

    for (let i = 0; i <= numPoints; i++) {
        const t = i / numPoints;
        const z = length * (t - 0.5);  // Linear interpolation in the z direction, normalized around 0

        // Smooth variations using sine and cosine waves with added smooth randomness
        const x = amplitudeX * Math.sin(frequency * z) + randomFactor * radius * smoothRandom(randomSeedX + t * 10);
        const y = amplitudeY * Math.sin(frequency * z * 0.5) + randomFactor * radius * smoothRandom(randomSeedY + t * 10);

        splinePoints.push(new THREE.Vector3(x, y, z));
    }

    return splinePoints;
}
// Simple smooth random function using Perlin noise-like behavior
function smoothRandom(seed) {
    const x = Math.sin(seed) * 10000;
    return x - Math.floor(x);
}

