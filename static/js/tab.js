//Tab Animation

const tabItems = document.querySelectorAll('.tab-items');
const backSpan = document.querySelector('.back-span');

const drag = document.querySelector('.drag');
const normal = document.querySelector('.normal');

let tabId;
[...tabItems].map(e => {
   e.addEventListener('click', () => {
        tabId = e.getAttribute('data-id');
        if(tabId === 'bulk'){
            backSpan.style = 'left: 121px; transition: left .3s ease';
            drag.classList.remove('hidden');
            normal.classList.add('hidden');
        }else if (tabId === 'single'){
            backSpan.style = 'left: 4px; transition: left .3s ease';
            drag.classList.add('hidden');
            normal.classList.remove('hidden');
        }
        else {
            backSpan.style = 'left: 4px; transition: left .3s ease';
            drag.classList.add('hidden');
            normal.classList.remove('hidden');
        }
   });
});

function readUrl(input) {

  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = (e) => {
      let imgData = e.target.result;
      let imgName = input.files[0].name;
      input.setAttribute("data-title", imgName);
      console.log(e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }

}