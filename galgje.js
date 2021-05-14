let filter;
let busy = false;
let todo = [];
let level = 1;
let finished = false;
let buttons = [];

let exclude = [];

newFilter();

function newFilter(){
    fetch(`cgi-bin/new_filter.cgi`)
        .then(antwoord => antwoord.json())
        .then(data => setFilter(data['filter']))
}


function guessLetter(letter, recursive = false) {
    if(!finished) {
        if (!busy || recursive) {
            exclude.push(letter);
            busy = true;
            const data = {value: letter, filter: filter, exclude:exclude};
            fetch(`cgi-bin/letter.cgi?data=${JSON.stringify(data)}`)
                .then(antwoord => antwoord.json())
                .then(data => handleGuess(data))
        } else {
            todo.push(letter);
        }
    }
}

function handleGuess(guess) {
    console.log(guess['filter'])
    if(guess['mistake']){
        wrong();
    }
    else if(guess['done']){
        done();
        setFilter(guess['filter'])
    }
    else {
        setFilter(guess['filter'])
    }

    if (todo.length > 0) {
        guessLetter(todo.shift(), true)
    } else {
        busy = false;
    }
}

function done() {
    finished = true;
    document.getElementById("word_container").classList.add("correct");
    disableAllButtons();
}

function wrong(){
    level += 1;
    load(level);
    if(level === 6){
        finished = true;
        dead();
    }
}

function dead() {
    document.getElementById("word_container").classList.add("dead");
    disableAllButtons();
}

function disableAllButtons() {
    buttons.forEach(function (a){
        disableButton(a);
    })
}

function setFilter(newFilter){
    filter = newFilter;
    let temp_filter = filter
    let wordDiv = document.getElementById("word_container")
    wordDiv.innerHTML = "";
    for (var i = 0; i < temp_filter.length; i++) {
        wordDiv.innerHTML += "<span class='letter-span'>" + temp_filter.charAt(i) + "</span>"
    }
}

for (i = 0; i < 26; i++) {
    const button = document.createElement("button");
    button.innerHTML = "Do Something";
    const letter = (i + 10).toString(36)
    button.innerHTML = letter.toUpperCase();
    button.classList.add("button");
    button.onclick = function (e){
        guessLetter(letter);
        disableButton(e.target);
    };
    document.getElementById("knoppen").appendChild(button);
    buttons.push(button);
}

function disableButton(button) {
    button.onclick = null;
    button.classList.add("button-disabled");
}