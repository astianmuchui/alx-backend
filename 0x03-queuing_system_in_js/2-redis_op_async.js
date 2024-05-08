#!/usr/bin/node
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();

client.on('connect', () =>
{
  console.log('Redis client connected to the server');
});

client.on('error', (error) =>
{
  console.error(`Redis client not connected to the server: ${error}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value)
{
  await setAsync(schoolName, value);
  console.log('School value set successfully');
}

async function displaySchoolValue(schoolName)
{
  const value = await getAsync(schoolName);
  console.log(value);
}

async function main()
{
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();