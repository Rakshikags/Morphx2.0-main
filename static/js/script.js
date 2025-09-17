console.log("Script loaded");

// Upvote functionality
function upvotePost(resourceId, btn) {
    fetch('/upvote', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({resource_id: resourceId})
    })
    .then(response => response.json())
    .then(data => {
        if (data.upvotes !== undefined) {
            btn.querySelector('.upvote-count').textContent = data.upvotes;
            btn.classList.add('upvoted');
            setTimeout(() => btn.classList.remove('upvoted'), 800);
        } else if (data.error) {
            alert(data.error);
        }
    });
}

// Show/hide password toggle (for login/register forms)
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.toggle-password').forEach(function(toggle) {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            if (input.type === "password") {
                input.type = "text";
                this.classList.add('fa-eye-slash');
                this.classList.remove('fa-eye');
            } else {
                input.type = "password";
                this.classList.add('fa-eye');
                this.classList.remove('fa-eye-slash');
            }
        });
    });
});