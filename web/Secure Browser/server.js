const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.set("view engine", "ejs");
app.use('/static', express.static('public'));

app.get('/', (req, res) => {
    res.render('index');
})

app.post('/', (req, res) => {
    var password = req.body.password;
    if (password === '5W$Fbb=+nBE*pg4t^7M') {
        res.send('wssqrctf{th1$_mU$t_b3_c0nfUs1ng}');
    } else {
        res.send('Failed! Try again.')
    }
});

app.listen(process.env.PORT || 3000, (req, res) => {
    console.log(`Listening on port ${
        process.env.PORT || 3000
    }`);
})
