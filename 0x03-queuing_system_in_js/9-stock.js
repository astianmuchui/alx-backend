#!/usr/bin/node


import express from 'express';
import redis from 'redis';
import { promisify } from 'util';


const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];


const getItemById = id => listProducts.find(product => product.itemId === id);


const app = express();
const PORT = 1245;


const client = redis.createClient();

client.on('error', err => {
  console.error(`Redis error: ${err}`);
});

const reserveStockById = (itemId, stock) => {
  client.set(`item_${itemId}`, stock);
};

const getCurrentReservedStockById = async itemId => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item_${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};


app.use(express.json());


app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({ ...product, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity >= product.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }
  reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});


app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});