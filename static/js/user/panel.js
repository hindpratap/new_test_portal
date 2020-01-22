
// Timer Countdown
let timer;
let savedDate = localStorage.getItem('savedDate');
let compareDate = new Date();
const monitorTime = document.querySelector('.monitor--time');

if (savedDate)  {
    compareDate = new Date(savedDate);
}
else {
    compareDate.setMinutes(compareDate.getMinutes() + 45); //Entered Time + 45 mins
    localStorage.setItem('savedDate', compareDate);
}

timer = setInterval(function() {
  timeBetweenDates(compareDate);
}, 1000);

function timeBetweenDates(toDate) {
  let dateEntered = toDate;
  let now = new Date();
  let difference = dateEntered.getTime() - now.getTime();

  if (difference <= 0) {
    // Timer done
    clearInterval(timer);

  } else {

    let seconds = Math.floor(difference / 1000);
    let minutes = Math.floor(seconds / 60);
    let hours = Math.floor(minutes / 60);

    hours %= 24;
    minutes %= 60;
    seconds %= 60;

    if(seconds <= 9){
        monitorTime.innerHTML = `${hours}:${minutes}:0${seconds}`;
    }else{
        monitorTime.innerHTML = `${hours}:${minutes}:${seconds}`;
    }

    if(minutes <= 5){
        monitorTime.style.color = 'tomato';
    }

    if(hours === 0 && minutes === 0 && seconds === 0){
        monitorTime.innerHTML = `0:00:00`;
        score();
        form.submit();
    }
  }
}


// Panels
const panel = document.querySelectorAll('.panel');
const nextBtn  = document.querySelector('#nextBtn');
const prevBtn = document.querySelector('#prevBtn');
const submitBtn = document.querySelector('#submitBtn');

const navSwitch = document.querySelectorAll('.switch__a');
navSwitch[0].style = 'background-color: royalblue; border: 2px solid royalblue; color: #fff;';

let counterPanel = 0;

panel[0].classList.remove('panel-hide');
prevBtn.style.display = 'none';

// Next Button
nextBtn.addEventListener('click', () => {
    prevBtn.style.display = "block";

    if(counterPanel < panel.length - 1){
        panel[counterPanel].classList.add('panel-hide');
        panel[counterPanel + 1].classList.remove('panel-hide');
        navigator(counterPanel);
        counterPanel++;
        navSwitch[counterPanel].style = 'background-color: royalblue; border: 2px solid royalblue; color: #fff;';
    }

    // When last panel reached change nextBtn type & text to submit
    if(counterPanel === (panel.length - 1)){
        nextBtn.classList.add('hidden');
        submitBtn.classList.remove('hidden');
    }

});

// Previous Button
prevBtn.addEventListener('click', () => {
    if(counterPanel > 0 ){
        panel[counterPanel-1].classList.remove('panel-hide');
        panel[counterPanel].classList.add('panel-hide');
        navigator(counterPanel);
        counterPanel--;
        navSwitch[counterPanel].style = 'background-color: royalblue; border: 2px solid royalblue; color: #fff;';
    }

    if(counterPanel === 0){
        prevBtn.style.display='none';
    }

    nextBtn.classList.remove('hidden');
    submitBtn.classList.add('hidden');
});

// Navigation

[...navSwitch].map(f => {
    f.addEventListener('click', () => {
        f.style = 'background-color: royalblue; border: 2px solid royalblue; color: #fff;';
        navigator(counterPanel);
        const num = parseInt(f.innerHTML);
        const dataComp = f.getAttribute('data-comp');

        [...panel].map(p => {
            const dataPan = p.getAttribute('data-id');

            if(dataPan === dataComp){
                p.classList.remove('panel-hide');

                if([...panel].indexOf(p) === 0){
                    prevBtn.style.display = 'none';
                    nextBtn.classList.remove('hidden');
                    submitBtn.classList.add('hidden');
                }else if([...panel].indexOf(p) === panel.length-1){
                    prevBtn.style.display = 'block';
                    nextBtn.classList.add('hidden');
                    submitBtn.classList.remove('hidden');
                }else{
                    prevBtn.style.display = 'block';
                    nextBtn.classList.remove('hidden');
                    submitBtn.classList.add('hidden');
                }

                counterPanel = [...panel].indexOf(p);
            }else{
                p.classList.add('panel-hide');
            }

        });

    });
});

// Play with lights
let navigator = (x) => {
    const opt = panel[x].querySelectorAll('.optBtn');
    const id = panel[x].getAttribute('data-id');
    let state = false;

    [...opt].map((e)=>{
        if(!state){
            if(e.checked) {
                [...navSwitch].map(z => {
                    const comp = z.getAttribute('data-comp');
                    if (id === comp) {
                        z.style = 'background-color: mediumaquamarine; border: 2px solid mediumaquamarine; color: #fff;';
                    }
                });
                state = true;
            }else{
                [...navSwitch].map(z => {
                    const comp = z.getAttribute('data-comp');
                    if (id === comp) {
                        z.style = 'background-color: tomato; border: 2px solid tomato; color: #fff;';
                    }
                });
            }
        }

    });
};

// Navigator Tab
const navCat = document.querySelectorAll('.nav-ques__h3');
[...navCat].map(m => {
    let clicked = false;
    m.addEventListener('click', () => {
        const s = m.nextElementSibling;
        if(!clicked){
            m.classList.add('clicked');
            s.style = `display: grid;`;
            clicked = true;
        }else{
            m.classList.remove('clicked');
            s.style = `display: none;`;
            clicked = false;
        }
    });
});
