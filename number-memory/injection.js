function listenBigNumbers(setNumber) {
    let interval = setInterval(() => {
        let $bigNumber = document.querySelector('.big-number');
        if (!$bigNumber) {
            return;
        }
        let num = $bigNumber.innerText;
        setNumber(num);
        clearInterval(interval);
    }, 10);

    return () => {
        clearInterval(interval);
    };
}

function enterNumber(num) {
    let interval = setInterval(() => {
        let $container = document.querySelector('.number-memory-test');
        let $input = $container.querySelector('input');
        if (!$input) {
            return;
        }
        $input.value = num;
        clearInterval(interval);
        hackMemoryTest();
    }, 10);

    return () => {
        clearInterval(interval);
    };
}

function hackMemoryTest() {
    listenBigNumbers(enterNumber);
}

hackMemoryTest();