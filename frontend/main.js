let token = localStorage.getItem('token')
//let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjYxNjYwLCJqdGkiOiI5YWE4MDRhMjU3MGQ0NTMzYTk4ZTY3OTYxY2M5ZTE1YiIsInVzZXJfaWQiOjF9.FqdxnxZCFTo8cjFp8lJyH7-XynSiYM0RriXgR3PQNnI"

let BarsUrl = 'http://127.0.0.1:8000/api/bars/'
let navBarWrapper = document.getElementById('nav-bar')
let barsWrapper = document.getElementById('bars--wrapper')

let buildPage = (Bars) => {
    //Render Nav Bar on Page
    navBarWrapper.innerHTML = ''    
    navBar = 
        `
            <button id="add-bar">Add Bar</button>
            <a href="login.html" id="login-btn">Login</a>
            <button id="logout-btn">Logout</button>
    
        `
    navBarWrapper.innerHTML = navBar
        
    let addBarBtn = document.getElementById('add-bar')
    let loginBtn = document.getElementById('login-btn')
    let logoutBtn = document.getElementById('logout-btn')

    if (token) {
        loginBtn.remove()
    } else {
        logoutBtn.remove()
    }

    addBarBtn.addEventListener('click', (e) => {
        e.preventDefault()
        window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/addBar.html'
    })
    logoutBtn.addEventListener('click', (e) => {
        e.preventDefault()
        localStorage.removeItem('token')
        window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/login.html'
    })


    //Render Bars_List on Page
    barsWrapper.innerHTML = ''
    for (let i = 0; Bars.length > i; i++) {
        let bar = Bars[i]
        let barCard = `
                <div class="bar--card">
                    <img src="http://127.0.0.1:8000${bar.photo_main}" />
                    
                    <div>
                        <div class="card--header">
                            <button class='soap-link' data-bar="${bar.id}" >${bar.name}</button>
                        </div>
                        <p>${bar.description.substring(0, 150)}</p>
                    </div>
                
                </div>
        `
        barsWrapper.innerHTML += barCard
    }

    //Add listener for each Bar button
    let barBtns = document.getElementsByClassName('soap-link')
    //console.log(barBtns)
    for (let i = 0; i < barBtns.length; i++) {
        barBtns[i].addEventListener('click', (e) => {
            //let token = localStorage.getItem('token')
            //let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjYxNjYwLCJqdGkiOiI5YWE4MDRhMjU3MGQ0NTMzYTk4ZTY3OTYxY2M5ZTE1YiIsInVzZXJfaWQiOjF9.FqdxnxZCFTo8cjFp8lJyH7-XynSiYM0RriXgR3PQNnI"
            //console.log(e.target.dataset.bar)
            let barId = e.target.dataset.bar

            fetch(`http://127.0.0.1:8000/api/bars/${barId}/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
            })
            .then(response => response.json())
            .then(data => {
                //console.log('Success:', data)
                bar = data

                //Render Nav Bar on Page
                navBarWrapper.innerHTML = ''
                navBar = 
                    `
                        <button id="get-bars">Home</button>
                        <a href="login.html" id="login-btn">Login</a>
                        <button id="logout-btn">Logout</button>
                
                    `
                navBarWrapper.innerHTML = navBar

                //Render Bar on Page
                barsWrapper.innerHTML = ''
                barCard = 
                    `
                    <div class="bar--card">
                        <img src="http://127.0.0.1:8000${bar.photo_main}" />
                        
                        <div>
                            <div class="card--header">
                                <button class='soap-link' data-bar="${bar.id}" >${bar.name}</button>
                            </div>
                            <p>${bar.description.substring(0, 150)}</p>
                        </div>
                    
                    </div>
                    `
                barsWrapper.innerHTML = barCard           
                
                let getBarsBtn = document.getElementById('get-bars')
                let loginBtn = document.getElementById('login-btn')
                let logoutBtn = document.getElementById('logout-btn')

                if (token) {
                    loginBtn.remove()
                } else {
                    logoutBtn.remove()
                }
                
                getBarsBtn.addEventListener('click', (e) => {
                    e.preventDefault()
                    getBars()
                })
                logoutBtn.addEventListener('click', (e) => {
                    e.preventDefault()
                    localStorage.removeItem('token')
                    window.location = 'file:///C:/Users/juang/webApps/08mlPythonApps/soapdish_project/frontend/login.html'
                })
            })
        })
    }
}

let getBars = () => {
    fetch(BarsUrl)
        .then(response => response.json())
        .then(data => {
            //console.log(data)
            buildPage(data)
        })
}

getBars()





