document.addEventListener('DOMContentLoaded', () => {


  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /////////////////////////////////////////// GET CSRF TOKEN //////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');


  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /////////////////////////////////////////// INITIALIZE STUFF ////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  let category = document.getElementById('category');
  let question = document.getElementById('question');
  let answer = document.getElementById('answer');
  let submit = document.getElementById('submit');

  question.style.display = 'none';
  answer.style.display = 'none';


  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /////////////////////////////////////////// GET QUESTIONS ///////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


  let questions_answered_arr = document.getElementById('questions_answered_pk').value.replace(/\s+/g, '').split(',');
  console.log(questions_answered_arr);
  let questions_answered = [];
  for (i = 0; i < questions_answered_arr.length; i++){
    questions_answered.push(parseInt(questions_answered_arr[i]));
  }

  async function getQuestions(e){
    console.log(e.target.value);

    fetch('/get_questions' + e.target.value)
    .then(response => response.json())
    .then(data => {
      console.log('Success: ', data);
      for (i = 0; i < data.length; i++){
        question.options[i+1] = new Option(data[i].question, data[i].id);
        if (questions_answered.includes(data[i].id)){
          question.options[i+1].disabled = true;
        }
      }
      question.style.display = 'block';
    })
    .catch((error) => {
      console.error('Error: ', error);
    });
  }

  category.addEventListener('input', getQuestions);


  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  //////////////////////////////////////////// GET ANSWERS ////////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  async function getAnswers(e){
    console.log(e.target)
    let data = { question_pk: e.target.value };

    fetch('/get_answers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success: ', data);
      for (i = 0; i < data.length; i++){
        answer.options[i+1] = new Option(data[i].answer, data[i].id);
      }
      answer.style.display = 'block'
    })
    .catch((error) => {
      console.error('Error: ', error);
    });
  }
  question.addEventListener('input', getAnswers);


  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  ///////////////////////////////////////// Enable/Disable SUBMIT /////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  answer.addEventListener('input', () => {
    submit.disabled = false;
  })


});
