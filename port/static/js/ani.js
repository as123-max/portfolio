document.addEventListener("DOMContentLoaded", function () {
    const numFireflies = 20;
    for (let i = 0; i < numFireflies; i++) {
        const firefly = document.createElement("div");
        firefly.classList.add("firefly");
        document.body.appendChild(firefly);
        firefly.style.top = Math.random() * window.innerHeight + "px";
        firefly.style.left = Math.random() * window.innerWidth + "px";
    }
});

