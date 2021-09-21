let token = localStorage.getItem('token')
//let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjYxNjYwLCJqdGkiOiI5YWE4MDRhMjU3MGQ0NTMzYTk4ZTY3OTYxY2M5ZTE1YiIsInVzZXJfaWQiOjF9.FqdxnxZCFTo8cjFp8lJyH7-XynSiYM0RriXgR3PQNnI"

let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')
let getBarsBtn = document.getElementById('get-bars')

let form = document.getElementById('addBar_form')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    //localStorage.removeItem('token')
    window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/login.html'
})

getBarsBtn.addEventListener('click', (e) => {
    e.preventDefault()
    window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/bars-list.html'
})

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let formData = {
        'creator': form.creator.value,
        'name': form.name.value,
        'recipe': form.recipe.value,
        'fragrance': form.fragrance.value,
        'batch_code': form.batch_code.value,
        'description': form.description.value,
        'colorants': form.colorants.value,
        'nutrients': form.nutrients.value,
        'exfolients': form.exfolients.value,
        'price': form.price.value,
        'discount': form.discount.value,
        'is_cured': form.is_cured.value,
    }

    fetch('http://127.0.0.1:8000/api/bars/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('DATA:', data)
            window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/bars-list.html'
        })
})