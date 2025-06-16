document.addEventListener('DOMContentLoaded', function() {
    const formContainer = document.getElementById('news-registration-form');
    const registerButton = document.getElementById('register-news-button');
    const cancelButton = document.getElementById('cancel-news-registration');
    
    if (!formContainer || !registerButton || !cancelButton) return;
    
    if (document.querySelector('.alert-danger') || document.querySelector('.alert-success')) {
        formContainer.style.display = 'block';
    }
    
    registerButton.addEventListener('click', function() {
        formContainer.style.display = 'block';
        formContainer.scrollIntoView({behavior: 'smooth'});
    });
    
    cancelButton.addEventListener('click', function() {
        formContainer.style.display = 'none';
    });
});