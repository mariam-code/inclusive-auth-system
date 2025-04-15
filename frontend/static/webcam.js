const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snapBtn = document.getElementById('snapBtn');

navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  })
  .catch((err) => {
    console.error("Camera access denied:", err);
  });

snapBtn.addEventListener('click', () => {
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  canvas.toBlob((blob) => {
    const formData = new FormData();
    formData.append('image', blob, 'capture.jpg');

    fetch('http://localhost:5003/verify-face', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      alert(data.match ? "✅ Face matched!" : "❌ Face not recognized.");
    })
    .catch(error => {
      alert("Error: " + error);
    });
  }, 'image/jpeg');
});
