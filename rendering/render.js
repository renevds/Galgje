// Setting scene for 3D Object
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
    75,
    1,
    0.1,
    1000);
var vector = new THREE.Vector3();
var renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(window.innerWidth, window.innerHeight);
container = document.getElementById("model");
renderer.setSize($(container).width(), $(container).height());
container.appendChild(renderer.domElement);

camera.position.set(0,0,15);

light = new THREE.DirectionalLight( 0xffffff );
light.intensity = 3;
camera.add(light);
scene.add(camera);

scene.background = null;
renderer.setClearColor(0x000000, 0);


const loader = new THREE.GLTFLoader();


let earth;


function load(number) {
    loader.load(
        'models/earth' + number + '.gltf',
        function (gltf) {
            if(earth !== undefined){
                scene.remove(earth)
            }
            earth = gltf.scene
            scene.add(gltf.scene);

            gltf.animations;
            gltf.scene;
            gltf.scenes;
            gltf.cameras;
            gltf.asset;
            light.target = gltf.scene

        },
        function (xhr) {

            //console.log((xhr.loaded / xhr.total * 100) + '% loaded');

        },
        function (error) {

        }
    );
}

load(1);

var animate = function () {
    requestAnimationFrame(animate);
    if(earth != undefined) {
        earth.rotation.y += 0.01;
        earth.rotation.y += 0.01;
        renderer.render(scene, camera);
    }
};

animate();