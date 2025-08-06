// static/js/main.js

document.addEventListener('DOMContentLoaded', function () {
    console.log("🟢 main.js loaded.");

    // Highlight active nav link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });

    // Show file name after resume file is selected
    const resumeInput = document.getElementById('resume');
    const fileLabel = document.getElementById('file-label');

    if (resumeInput && fileLabel) {
        resumeInput.addEventListener('change', function () {
            const fileName = this.files[0]?.name || "No file selected";
            fileLabel.textContent = fileName;
        });
    }

    // Simple form validation (optional)
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                alert("Please fill out all required fields.");
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Toggle password visibility
    const togglePass = document.getElementById("toggle-password");
    const passwordInput = document.getElementById("password");

    if (togglePass && passwordInput) {
        togglePass.addEventListener("click", function () {
            const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
            passwordInput.setAttribute("type", type);
            this.classList.toggle("fa-eye");
            this.classList.toggle("fa-eye-slash");
        });
    }
});
