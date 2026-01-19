
// Animación de partículas de fondo (simple, sin librerías externas)
document.addEventListener('DOMContentLoaded', () => {
	const canvas = document.createElement('canvas');
	canvas.id = 'particles-bg';
	canvas.style.position = 'fixed';
	canvas.style.top = 0;
	canvas.style.left = 0;
	canvas.style.width = '100vw';
	canvas.style.height = '100vh';
	canvas.style.zIndex = 0;
	canvas.style.pointerEvents = 'none';
	document.body.appendChild(canvas);

	const ctx = canvas.getContext('2d');
	let particles = [];
	const colors = ['#2e7d32', '#f1c40f', '#2c6e49', '#388e3c'];
	const numParticles = 40;

	function resizeCanvas() {
		canvas.width = window.innerWidth;
		canvas.height = window.innerHeight;
	}
	window.addEventListener('resize', resizeCanvas);
	resizeCanvas();

	function createParticles() {
		particles = [];
		for (let i = 0; i < numParticles; i++) {
			particles.push({
				x: Math.random() * canvas.width,
				y: Math.random() * canvas.height,
				r: 2 + Math.random() * 3,
				dx: -0.5 + Math.random(),
				dy: -0.5 + Math.random(),
				color: colors[Math.floor(Math.random() * colors.length)]
			});
		}
	}
	createParticles();

	function animateParticles() {
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		for (let p of particles) {
			ctx.beginPath();
			ctx.arc(p.x, p.y, p.r, 0, 2 * Math.PI);
			ctx.fillStyle = p.color;
			ctx.globalAlpha = 0.5;
			ctx.fill();
			ctx.globalAlpha = 1;
			p.x += p.dx;
			p.y += p.dy;
			if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
			if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
		}
		requestAnimationFrame(animateParticles);
	}
	animateParticles();

	// Animación de botones CTA
	document.querySelectorAll('.cta-btn').forEach(btn => {
		btn.addEventListener('mouseenter', () => {
			btn.classList.add('animate__pulse');
		});
		btn.addEventListener('mouseleave', () => {
			btn.classList.remove('animate__pulse');
		});
		btn.addEventListener('mousedown', () => {
			btn.style.transform = 'scale(0.96)';
		});
		btn.addEventListener('mouseup', () => {
			btn.style.transform = '';
		});
	});
});
