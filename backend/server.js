const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const multer = require('multer');
const upload = multer();

const productRoute = require('./routes/api/productRoute');

// Connecting to the Database
let mongodb_url = 'mongodb://localhost/';
let dbName = 'yolomy';

const MONGODB_URI = 'mongodb://mongo-db:27017/yolomy';  // mongo-db is the container name// const MONGODB_URI = process.env.MONGODB_URI || 'mongodb+srv://james_rashid:james_rashid@cluster0.bwtll.mongodb.net/yolomy?retryWrites=true&w=majority&appName=Cluster0'
//const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/yolomy';
mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
let db = mongoose.connection;

// Check Connection
db.once('open', ()=>{
    console.log('Database connected successfully')
})

// Check for DB Errors
db.on('error', (error)=>{
    console.log(error);
})

// Initializing express
const app = express()

// Body parser middleware
app.use(express.json())

// 
app.use(upload.array()); 

// Cors 
app.use(cors());

// Use Route
app.use('/api/products', productRoute)

// Define the PORT
const PORT = process.env.PORT || 5000

app.listen(PORT, ()=>{
    console.log(`Server listening on port ${PORT}`)
})
