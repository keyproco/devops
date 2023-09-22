const express = require('express');


const app = express();


app.get('/', (req, res) => {
    res.send('Hello Thomas');
});

app.listen(3000, () => {
    console.log('On est entrain d ecouter le port 3000')
});


