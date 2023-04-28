let canvas = document.getElementById('canvas');
ctx = canvas.getContext("2d");
function clearCanvas() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, 600, 600);
}
clearCanvas();

let mousedown = false;
addEventListener('mousedown', () => {
    mousedown = true;
});

addEventListener('mouseup', () => {
    mousedown = false;
})

addEventListener('mousemove', e => {
   if (mousedown) {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        ctx.beginPath();
        ctx.arc(x, y, 25, 0, Math.PI * 2, false);
        var grd = ctx.createRadialGradient(x, y, 10, x, y, 25);
        grd.addColorStop(0, "white");
        grd.addColorStop(1, "rgba(255, 255, 255, 0)");
        ctx.fillStyle = grd;
        ctx.fill();
   }
});