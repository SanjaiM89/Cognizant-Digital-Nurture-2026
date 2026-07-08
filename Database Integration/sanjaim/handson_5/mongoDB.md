
```
test> use college_nosql
switched to db college_nosql
college_nosql> d.createCollection('feedback')
ReferenceError: d is not defined
college_nosql> db.createCollection('feedback')
{ ok: 1 }
college_nosql> show dbs
admin          100.00 KiB
college_nosql    8.00 KiB
config          92.00 KiB
local           72.00 KiB
college_nosql> show collections
feedback
college_nosql> 
```
 **Task 1: Create the Collection and Insert Documents**

 ``` javascript
 use college_nosql
 switched to db college_nosql
 db["feedback"].find()
  
 db.feedback.insertMany([
   {
     student_id: 1,
     course_code: 'CS101',
     semester: '2026-ODD',
     rating: 4,
     comments: 'Excellent teaching. Would recommend.',
     tags: ['challenging', 'well-structured', 'good-examples'],
     submitted_at: new Date('2026-11-30T10:15:00Z'),
     attachments: [{ filename: 'name.pdf', size_kb: 240 }]
   },
   {
     student_id: 2,
     course_code: 'CS101',
     semester: '2026-ODD',
     rating: 5,
     comments: 'Best course this semester, very clear explanations.',
     tags: ['well-structured', 'engaging'],
     submitted_at: new Date('2026-11-30T11:00:00Z'),
     attachments: [{ filename: 'name1.pdf', size_kb: 85 }]
   },
   {
     student_id: 3,
     course_code: 'CS101',
     semester: '2026-EVEN',
     rating: 2,
     comments: 'Pace was too fast, hard to keep up with assignments.',
     tags: ['challenging', 'fast-paced'],
     submitted_at: new Date('2026-05-14T09:30:00Z'),
     attachments: [{ filename: 'name2.pdf', size_kb: 120 }]
   },
   {
     student_id: 4,
     course_code: 'CS102',
     semester: '2026-ODD',
     rating: 3,
     comments: 'Average course, could use more practical examples.',
     tags: ['average', 'needs-examples'],
     submitted_at: new Date('2026-11-29T14:20:00Z'),
     attachments: [{ filename: 'name3.pdf', size_kb: 300 }]
   },
   {
     student_id: 5,
     course_code: 'CS102',
     semester: '2026-EVEN',
     rating: 5,
     comments: 'Loved the hands-on labs and project work.',
     tags: ['hands-on', 'well-structured', 'good-examples'],
     submitted_at: new Date('2026-05-15T16:45:00Z'),
     attachments: [{ filename: 'name4.pdf', size_kb: 512 }]
   },
   {
     student_id: 6,
     course_code: 'CS103',
     semester: '2026-ODD',
     rating: 1,
     comments: 'Very disorganized, unclear grading criteria.',
     tags: ['disorganized', 'unclear-grading'],
     submitted_at: new Date('2026-11-28T08:10:00Z'),
     attachments: [{ filename: 'name5.pdf', size_kb: 45 }]
   },
   {
     student_id: 7,
     course_code: 'CS104',
     semester: '2026-EVEN',
     rating: 4,
     comments: 'Good balance of theory and practice.',
     tags: ['balanced', 'good-examples'],
     submitted_at: new Date('2026-05-16T10:05:00Z'),
     attachments: [{ filename: 'name6.pdf', size_kb: 190 }]
   },
   {
     student_id: 8,
     course_code: 'CS101',
     semester: '2026-EVEN',
     rating: 3,
     comments: 'Decent, but assignments were repetitive.',
     tags: ['repetitive', 'average'],
     submitted_at: new Date('2026-05-17T12:30:00Z'),
     attachments: [{ filename: 'name7.pdf', size_kb: 75 }]
   },
   {
     student_id: 9,
     course_code: 'CS105',
     semester: '2026-ODD',
     rating: 5,
     comments: 'Instructor was very approachable and helpful.',
     tags: ['engaging', 'well-structured'],
     submitted_at: new Date('2026-11-27T13:15:00Z'),
     attachments: [{ filename: 'name8.pdf', size_kb: 210 }]
   },
   {
     student_id: 10,
     course_code: 'CS102',
     semester: '2026-ODD',
     rating: 2,
     comments: 'Course content felt outdated compared to industry practice.',
     tags: ['outdated', 'needs-update'],
     submitted_at: new Date('2026-11-26T15:50:00Z'),
     attachments: [{ filename: 'name9.pdf', size_kb: 150 }]
   }
 ])
 {
   acknowledged: true,
   insertedIds: {
     '0': ObjectId('6a4e67fda029b2b3f8dee432'),
     '1': ObjectId('6a4e67fda029b2b3f8dee433'),
     '2': ObjectId('6a4e67fda029b2b3f8dee434'),
     '3': ObjectId('6a4e67fda029b2b3f8dee435'),
     '4': ObjectId('6a4e67fda029b2b3f8dee436'),
     '5': ObjectId('6a4e67fda029b2b3f8dee437'),
     '6': ObjectId('6a4e67fda029b2b3f8dee438'),
     '7': ObjectId('6a4e67fda029b2b3f8dee439'),
     '8': ObjectId('6a4e67fda029b2b3f8dee43a'),
     '9': ObjectId('6a4e67fda029b2b3f8dee43b')
   }
 }
 db.feedback.insertOne(
   {
     student_id: 11,
     course_code: 'CS101',
     semester: '2026-EVEN',
     rating: 4,
     comments: 'Solid course overall, enjoyed the assignments.',
     tags: ['well-structured', 'engaging'],
     submitted_at: new Date('2026-05-18T09:00:00Z')
   }
 )
 {
   acknowledged: true,
   insertedId: ObjectId('6a4e681da029b2b3f8dee43c')
 }
 db.feedback.countDocuments()
 11
 college_nosql
 
 ```