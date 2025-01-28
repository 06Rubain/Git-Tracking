// Gestion du thème sombre et clair
document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;

    // Charger le thème depuis localStorage
    const savedTheme = localStorage.getItem('theme') || 'light';
    body.classList.add(savedTheme + '-theme');

    // Mettre à jour le bouton au chargement
    updateButton(savedTheme);

    themeToggle.addEventListener('click', function () {
        const currentTheme = body.classList.contains('light-theme') ? 'light' : 'dark';

        // Basculer entre les thèmes
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        body.classList.remove(currentTheme + '-theme');
        body.classList.add(newTheme + '-theme');

        // Sauvegarder le thème dans localStorage
        localStorage.setItem('theme', newTheme);

        // Mettre à jour le bouton
        updateButton(newTheme);
    });

    function updateButton(theme) {
        themeToggle.innerHTML = theme === 'light'
            ? '<i class="fas fa-moon"></i> Thème Sombre'
            : '<i class="fas fa-sun"></i> Thème Clair';
    }
});


// Activer la caméra
document.getElementById('start-camera').addEventListener('click', function () {
    const cameraContainer = document.getElementById('camera');
    const html5QrCode = new Html5Qrcode("camera");

    html5QrCode.start({ facingMode: "environment" }, {}, () => {
        console.log("Caméra activée !");
    });
});

// Capture de la photo
document.getElementById('capture-photo').addEventListener('click', function () {
    const capturedImageInput = document.getElementById('captured-image');
    // Implémente ici la capture d'image en base64 et l'assigne à `capturedImageInput.value`.
    console.log("Photo capturée !");
});

