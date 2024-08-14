


document.addEventListener('DOMContentLoaded', function() {
    const audios = document.querySelectorAll('audio');
    
    for (let i = 0; i < audios.length; i++) {
        audios[i].addEventListener('ended', function() {
            if (i + 1 < audios.length) {
                audios[i + 1].play();
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const audios = document.querySelectorAll('audio');

    audios.forEach((audio, index) => {
        const currentTimeDisplay = document.getElementById(`current-time${index + 1}`);

        // Обновляем отображение текущего времени трека
        audio.addEventListener('timeupdate', function() {
            const minutes = Math.floor(audio.currentTime / 60);
            const seconds = Math.floor(audio.currentTime % 60);
            currentTimeDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        });
    });
});