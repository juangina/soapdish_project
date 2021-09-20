let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_bar/frontend/login.html'
})



let BarsUrl = 'http://127.0.0.1:8000/api/bars/'

let getBars = () => {

    fetch(BarsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildBars(data)
        })

}

let buildBars = (Bars) => {
    let BarsWrapper = document.getElementById('bars--wrapper')
    BarsWrapper.innerHTML = ''
    for (let i = 0; Bars.length > i; i++) {
        let bar = Bars[i]

        let barCard = `
                <div class="bar--card">
                    <img src="http://127.0.0.1:8000${bar.photo_main}" />
                    
                    <div>
                        <div class="card--header">
                            <h3>${bar.name}</h3>
                        </div>
                        <p>${bar.description.substring(0, 150)}</p>
                    </div>
                
                </div>
        `
        BarsWrapper.innerHTML += barCard
    }

    //Add an listener
}

getBars()