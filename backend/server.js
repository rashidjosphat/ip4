const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const multer = require('multer');
const upload = multer();

const productRoute = require('./routes/api/productRoute');

// Connecting to the Database
let mongodb_url = 'mongodb://localhost/';
let dbName = 'yolomy';

const MONGODB_URI = 'mongodb://mongodb-0.mongodb:27017/yolomy'; // MongoDB URI
mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
let db = mongoose.connection;

// Check Connection
db.once('open', () => {
    console.log('Database connected successfully')
})

// Check for DB Errors
db.on('error', (error) => {
    console.log(error);
})

// Initializing express
const app = express()

// Body parser middleware
app.use(express.json())

// Upload middleware
app.use(upload.array());

// CORS configuration to allow any origin
app.use(cors());

// Use Route
app.use('/api/products', productRoute);

// Define the PORT
const PORT = process.env.PORT || 5000

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`)
})
