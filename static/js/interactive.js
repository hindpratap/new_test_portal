// Fetch Components
try{
    const passwordEye = document.querySelector(`.password-eye`);
    const passwordInput = document.querySelector(`[name='password']`);

    let passwordState = false;

    passwordEye.addEventListener('click', ()=>{
        console.log('work');
        if(passwordState){
            passwordEye.innerHTML = `<i class="fas fa-eye-slash"></i>`;
            passwordEye.setAttribute('title', 'Hide Password');
            passwordInput.setAttribute('type', 'password');
            passwordState = false;
        }else{
            passwordEye.innerHTML = `<i class="fas fa-eye"></i>`;
            passwordEye.setAttribute('type', 'Show Password');
            passwordInput.setAttribute('type', 'text');
            passwordState = true;
        }
    });
}catch(err){}

// Instruction Components
try{

    // Report
    const assessLink = document.querySelector('.assess-link');
    const reportLink = document.querySelector('.report-link');
    const reportDiv = document.querySelector('.report');
    const radioDiv = document.querySelectorAll('.error-type__radio');
    const cross = document.querySelector('.cross');

    reportLink.addEventListener('click', ()=>{
        reportLink.classList.add('active');
        assessLink.classList.remove('active');
        reportDiv.style.visibility = 'visible';
    });

    function reportState(e){
        let radioBtn = e.querySelector(`[name='whichErr']`);
        radioBtn.checked = true;

        Array.from(radioDiv).forEach((div)=>{
            div.classList.remove('err__active');
        });

        e.classList.add('err__active');
        console.log(e.classList);
    }

    cross.addEventListener('click', ()=>{
        reportDiv.style.visibility = 'hidden';
        assessLink.classList.add('active');
        reportLink.classList.remove('active');
    });

    // Continue/Start
    const startBtn = document.querySelector('.start-test');
    const startDiv = document.querySelector('.start');
    const cancelNo = document.querySelector('.cancel-no');

    startBtn.addEventListener('click', (e)=>{
        startDiv.style.visibility = 'visible';
    });

    cancelNo.addEventListener('click', (e)=>{
        startDiv.style.visibility = 'hidden';
    });

}catch(err){}