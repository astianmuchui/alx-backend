#!/usr/bin/node
const kue = require('kue');


const blacklistedNumbers = ['4153518780', '4153518781'];


function sendNotification(phoneNumber, message, job, done) {
  
  job.progress(0, 100);

  
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  
  job.progress(50, 100);

  
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  
  done();
}


const queue = kue.createQueue({ concurrency: 2 }); 


queue.process('push_notification_code_2', 2, (job, done) => {
  
  const { phoneNumber, message } = job.data;

  
  sendNotification(phoneNumber, message, job, done);

  
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
