import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {

    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 } });
    queue.testMode.enter();
  });

  afterEach(() => {

    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('creates two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 5678 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);


    expect(queue.testMode.jobs.length).to.equal(2);
  });
});