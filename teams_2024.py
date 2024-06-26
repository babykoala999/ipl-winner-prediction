import pandas as pd

players = [
    {'Player': 'Rohit Sharma', 'Team': 'MI'},
    {'Player': 'Dewald Brevis', 'Team': 'MI'},
    {'Player': 'Suryakumar Yadav', 'Team': 'MI'},
    {'Player': 'Ishan Kishan', 'Team': 'MI'},
    {'Player': 'Tilak Verma', 'Team': 'MI'},
    {'Player': 'Tim David', 'Team': 'MI'},
    {'Player': 'Vishnu Vinod', 'Team': 'MI'},
    {'Player': 'Arjun Tendulkar', 'Team': 'MI'},
    {'Player': 'Hardik Pandya', 'Team': 'MI'},
    {'Player': 'Shams Mulani', 'Team': 'MI'},
    {'Player': 'Nehal Wadhera', 'Team': 'MI'},
    {'Player': 'Jasprit Bumrah', 'Team': 'MI'},
    {'Player': 'Kumar Kartikeya', 'Team': 'MI'},
    {'Player': 'Piyush Chawla', 'Team': 'MI'},
    {'Player': 'Akash Madhwal', 'Team': 'MI'},
    {'Player': 'Jason Behrendorff', 'Team': 'MI'},
    {'Player': 'Romario Shepherd', 'Team': 'MI'},
    {'Player': 'Gerald Coetzee', 'Team': 'MI'},
    {'Player': 'Dilshan Madushanka', 'Team': 'MI'},
    {'Player': 'Shreyas Gopal', 'Team': 'MI'},
    {'Player': 'Nuwan Thushara', 'Team': 'MI'},
    {'Player': 'Naman Dhir', 'Team': 'MI'},
    {'Player': 'Anshul Kamboj', 'Team': 'MI'},
    {'Player': 'Mohammad Nabi', 'Team': 'MI'},
    {'Player': 'Shivalik Sharma', 'Team': 'MI'},
    {'Player': 'MS Dhoni', 'Team': 'CSK'},
    {'Player': 'Moeen Ali', 'Team': 'CSK'},
    {'Player': 'Deepak Chahar', 'Team': 'CSK'},
    {'Player': 'Devon Conway', 'Team': 'CSK'},
    {'Player': 'Tushar Deshpande', 'Team': 'CSK'},
    {'Player': 'Shivam Dube', 'Team': 'CSK'},
    {'Player': 'Ruturaj Gaikwad', 'Team': 'CSK'},
    {'Player': 'Rajvardhan Hangargekar', 'Team': 'CSK'},
    {'Player': 'Ravindra Jadeja', 'Team': 'CSK'},
    {'Player': 'Ajay Mandal', 'Team': 'CSK'},
    {'Player': 'Mukesh Choudhary', 'Team': 'CSK'},
    {'Player': 'Matheesha Pathirana', 'Team': 'CSK'},
    {'Player': 'Ajinkya Rahane', 'Team': 'CSK'},
    {'Player': 'Shaik Rasheed', 'Team': 'CSK'},
    {'Player': 'Mitchell Santner', 'Team': 'CSK'},
    {'Player': 'Simarjeet Singh', 'Team': 'CSK'},
    {'Player': 'Nishant Sindhu', 'Team': 'CSK'},
    {'Player': 'Prashant Solanki', 'Team': 'CSK'},
    {'Player': 'Maheesh Theekshana', 'Team': 'CSK'},
    {'Player': 'Daryl Mitchell', 'Team': 'CSK'},
    {'Player': 'Sameer Rizvi', 'Team': 'CSK'},
    {'Player': 'Mustafizur Rahman', 'Team': 'CSK'},
    {'Player': 'Avanish Rao Aravelly', 'Team': 'CSK'},
    {'Player': 'Shubman Gill', 'Team': 'GT'},
    {'Player': 'David Miller', 'Team': 'GT'},
    {'Player': 'Matthew Wade', 'Team': 'GT'},
    {'Player': 'Wriddhiman Saha', 'Team': 'GT'},
    {'Player': 'Kane Williamson', 'Team': 'GT'},
    {'Player': 'Abhinav Manohar', 'Team': 'GT'},
    {'Player': 'B. Sai Sudharsan', 'Team': 'GT'},
    {'Player': 'Darshan Nalkande', 'Team': 'GT'},
    {'Player': 'Vijay Shankar', 'Team': 'GT'},
    {'Player': 'Jayant Yadav', 'Team': 'GT'},
    {'Player': 'Rahul Tewatia', 'Team': 'GT'},
    {'Player': 'Mohammed Shami', 'Team': 'GT'},
    {'Player': 'Noor Ahmad', 'Team': 'GT'},
    {'Player': 'R. Sai Kishore', 'Team': 'GT'},
    {'Player': 'Rashid Khan', 'Team': 'GT'},
    {'Player': 'Joshua Little', 'Team': 'GT'},
    {'Player': 'Mohit Sharma', 'Team': 'GT'},
    {'Player': 'Azmatullah Omarzai', 'Team': 'GT'},
    {'Player': 'Umesh Yadav', 'Team': 'GT'},
    {'Player': 'Shahrukh Khan', 'Team': 'GT'},
    {'Player': 'Sushant Mishra', 'Team': 'GT'},
    {'Player': 'Kartik Tyagi', 'Team': 'GT'},
    {'Player': 'Manav Suthar', 'Team': 'GT'},
    {'Player': 'Spencer Johnson', 'Team': 'GT'},
    {'Player': 'Robin Minz', 'Team': 'GT'},
    {'Player': 'Rishabh Pant', 'Team': 'DC'},
    {'Player': 'Pravin Dubey', 'Team': 'DC'},
    {'Player': 'David Warner', 'Team': 'DC'},
    {'Player': 'Vicky Ostwal', 'Team': 'DC'},
    {'Player': 'Prithvi Shaw', 'Team': 'DC'},
    {'Player': 'Anrich Nortje', 'Team': 'DC'},
    {'Player': 'Abishek Porel', 'Team': 'DC'},
    {'Player': 'Kuldeep Yadav', 'Team': 'DC'},
    {'Player': 'Axar Patel', 'Team': 'DC'},
    {'Player': 'Lungi Ngidi', 'Team': 'DC'},
    {'Player': 'Lalit Yadav', 'Team': 'DC'},
    {'Player': 'Khaleel Ahmed', 'Team': 'DC'},
    {'Player': 'Mitchell Marsh', 'Team': 'DC'},
    {'Player': 'Ishant Sharma', 'Team': 'DC'},
    {'Player': 'Yash Dhull', 'Team': 'DC'},
    {'Player': 'Mukesh Kumar', 'Team': 'DC'},
    {'Player': 'Harry Brook', 'Team': 'DC'},
    {'Player': 'Tristan Stubbs', 'Team': 'DC'},
    {'Player': 'Ricky Bhui', 'Team': 'DC'},
    {'Player': 'Kumar Kushagra', 'Team': 'DC'},
    {'Player': 'Rasikh Dar', 'Team': 'DC'},
    {'Player': 'Jhye Richardson', 'Team': 'DC'},
    {'Player': 'Sumit Kumar', 'Team': 'DC'},
    {'Player': 'Shai Hope', 'Team': 'DC'},
    {'Player': 'Swastik Chhikara', 'Team': 'DC'},
    {'Player': 'KL Rahul', 'Team': 'LSG'},
    {'Player': 'Quinton de Kock', 'Team': 'LSG'},
    {'Player': 'Nicholas Pooran', 'Team': 'LSG'},
    {'Player': 'Ayush Badoni', 'Team': 'LSG'},
    {'Player': 'Kyle Mayers', 'Team': 'LSG'},
    {'Player': 'Marcus Stoinis', 'Team': 'LSG'},
    {'Player': 'Deepak Hooda', 'Team': 'LSG'},
    {'Player': 'Ravi Bishnoi', 'Team': 'LSG'},
    {'Player': 'Naveen-ul-Haq', 'Team': 'LSG'},
    {'Player': 'Krunal Pandya', 'Team': 'LSG'},
    {'Player': 'Yudhvir Singh', 'Team': 'LSG'},
    {'Player': 'Prerak Mankad', 'Team': 'LSG'},
    {'Player': 'Yash Thakur', 'Team': 'LSG'},
    {'Player': 'Amit Mishra', 'Team': 'LSG'},
    {'Player': 'Mark Wood', 'Team': 'LSG'},
    {'Player': 'Mayank Yadav', 'Team': 'LSG'},
    {'Player': 'Mohsin Khan', 'Team': 'LSG'},
    {'Player': 'Shivam Mavi', 'Team': 'LSG'},
    {'Player': 'Arshin Kulkarni', 'Team': 'LSG'},
    {'Player': 'M Siddharth', 'Team': 'LSG'},
    {'Player': 'Ashton Turner', 'Team': 'LSG'},
    {'Player': 'David Willey', 'Team': 'LSG'},
    {'Player': 'Mohd. Arshad Khan', 'Team': 'LSG'},
    {'Player': 'Sanju Samson', 'Team': 'RR'},
    {'Player': 'Jos Buttler', 'Team': 'RR'},
    {'Player': 'Shimron Hetmyer', 'Team': 'RR'},
    {'Player': 'Yashasvi Jaiswal', 'Team': 'RR'},
    {'Player': 'Dhruv Jurel', 'Team': 'RR'},
    {'Player': 'Riyan Parag', 'Team': 'RR'},
    {'Player': 'Donovan Ferreira', 'Team': 'RR'},
    {'Player': 'Kunal Rathore', 'Team': 'RR'},
    {'Player': 'Ravichandran Ashwin', 'Team': 'RR'},
    {'Player': 'Kuldeep Sen', 'Team': 'RR'},
    {'Player': 'Navdeep Saini', 'Team': 'RR'},
    {'Player': 'Prasidh Krishna', 'Team': 'RR'},
    {'Player': 'Sandeep Sharma', 'Team': 'RR'},
    {'Player': 'Trent Boult', 'Team': 'RR'},
    {'Player': 'Yuzvendra Chahal', 'Team': 'RR'},
    {'Player': 'Adam Zampa', 'Team': 'RR'},
    {'Player': 'Avesh Khan', 'Team': 'RR'},
    {'Player': 'Rovman Powell', 'Team': 'RR'},
    {'Player': 'Shubham Dubey', 'Team': 'RR'},
    {'Player': 'Tom Kohler-Cadmore', 'Team': 'RR'},
    {'Player': 'Abid Mushtaq', 'Team': 'RR'},
    {'Player': 'Nandre Burger', 'Team': 'RR'},
    {'Player': 'Abdul Samad', 'Team': 'SRH'},
    {'Player': 'Abhishek Sharma', 'Team': 'SRH'},
    {'Player': 'Aiden Markram', 'Team': 'SRH'},
    {'Player': 'Marco Jansen', 'Team': 'SRH'},
    {'Player': 'Rahul Tripathi', 'Team': 'SRH'},
    {'Player': 'Washington Sundar', 'Team': 'SRH'},
    {'Player': 'Glenn Phillips', 'Team': 'SRH'},
    {'Player': 'Sanvir Singh', 'Team': 'SRH'},
    {'Player': 'Heinrich Klaasen', 'Team': 'SRH'},
    {'Player': 'Bhuvneshwar Kumar', 'Team': 'SRH'},
    {'Player': 'Mayank Agarwal', 'Team': 'SRH'},
    {'Player': 'T Natarajan', 'Team': 'SRH'},
    {'Player': 'Anmolpreet Singh', 'Team': 'SRH'},
    {'Player': 'Mayank Markande', 'Team': 'SRH'},
    {'Player': 'Upendra Singh Yadav', 'Team': 'SRH'},
    {'Player': 'Umran Malik', 'Team': 'SRH'},
    {'Player': 'Nitish Kumar Reddy', 'Team': 'SRH'},
    {'Player': 'Fazalhaq Farooqi', 'Team': 'SRH'},
    {'Player': 'Shahbaz Ahmed', 'Team': 'SRH'},
    {'Player': 'Travis Head', 'Team': 'SRH'},
    {'Player': 'Wanindu Hasaranga', 'Team': 'SRH'},
    {'Player': 'Pat Cummins', 'Team': 'SRH'},
    {'Player': 'Jaydev Unadkat', 'Team': 'SRH'},
    {'Player': 'Akash Singh', 'Team': 'SRH'},
    {'Player': 'Jhathavedh Subramanyan', 'Team': 'SRH'},
     {'Player': 'Faf du Plessis', 'Team': 'RCB'},
    {'Player': 'Glenn Maxwell', 'Team': 'RCB'},
    {'Player': 'Virat Kohli', 'Team': 'RCB'},
    {'Player': 'Rajat Patidar', 'Team': 'RCB'},
    {'Player': 'Anuj Rawat', 'Team': 'RCB'},
    {'Player': 'Dinesh Karthik', 'Team': 'RCB'},
    {'Player': 'Suyash Prabhudessai', 'Team': 'RCB'},
    {'Player': 'Will Jacks', 'Team': 'RCB'},
    {'Player': 'Mahipal Lomror', 'Team': 'RCB'},
    {'Player': 'Karn Sharma', 'Team': 'RCB'},
    {'Player': 'Manoj Bhandage', 'Team': 'RCB'},
    {'Player': 'Mohammed Siraj', 'Team': 'RCB'},
    {'Player': 'Reece Topley', 'Team': 'RCB'},
    {'Player': 'Himanshu Sharma', 'Team': 'RCB'},
    {'Player': 'Rajan Kumar', 'Team': 'RCB'},
    {'Player': 'Cameron Green', 'Team': 'RCB'},
    {'Player': 'Alzarri Joseph', 'Team': 'RCB'},
    {'Player': 'Yash Dayal', 'Team': 'RCB'},
    {'Player': 'Tom Curran', 'Team': 'RCB'},
    {'Player': 'Lockie Ferguson', 'Team': 'RCB'},
    {'Player': 'Swapnil Singh', 'Team': 'RCB'},
    {'Player': 'Saurav Chuahan', 'Team': 'RCB'},
    {'Player': 'Shikhar Dhawan', 'Team': 'PBKS'},
    {'Player': 'Matthew Short', 'Team': 'PBKS'},
    {'Player': 'Prabhsimran Singh', 'Team': 'PBKS'},
    {'Player': 'Jitesh Sharma', 'Team': 'PBKS'},
    {'Player': 'Sikandar Raza', 'Team': 'PBKS'},
    {'Player': 'Rishi Dhawan', 'Team': 'PBKS'},
    {'Player': 'Liam Livingstone', 'Team': 'PBKS'},
    {'Player': 'Atharva Taide', 'Team': 'PBKS'},
    {'Player': 'Arshdeep Singh', 'Team': 'PBKS'},
    {'Player': 'Nathan Ellis', 'Team': 'PBKS'},
    {'Player': 'Sam Curran', 'Team': 'PBKS'},
    {'Player': 'Kagiso Rabada', 'Team': 'PBKS'},
    {'Player': 'Harpreet Brar', 'Team': 'PBKS'},
    {'Player': 'Rahul Chahar', 'Team': 'PBKS'},
    {'Player': 'Harpreet Bhatia', 'Team': 'PBKS'},
    {'Player': 'Vidwath Kaverappa', 'Team': 'PBKS'},
    {'Player': 'Shivam Singh', 'Team': 'PBKS'},
    {'Player': 'Harshal Patel', 'Team': 'PBKS'},
    {'Player': 'Chris Woakes', 'Team': 'PBKS'},
    {'Player': 'Ashutosh Sharma', 'Team': 'PBKS'},
    {'Player': 'Vishwanath Pratap Singh', 'Team': 'PBKS'},
    {'Player': 'Shashank Singh', 'Team': 'PBKS'},
    {'Player': 'Tanay Thyagarajann', 'Team': 'PBKS'},
    {'Player': 'Prince Choudhary', 'Team': 'PBKS'},
    {'Player': 'Rilee Rossouw', 'Team': 'PBKS'},
    {'Player': 'Nitish Rana', 'Team': 'KKR'},
    {'Player': 'Rinku Singh', 'Team': 'KKR'},
    {'Player': 'Rahmanullah Gurbaz', 'Team': 'KKR'},
    {'Player': 'Shreyas Iyer', 'Team': 'KKR'},
    {'Player': 'Jason Roy', 'Team': 'KKR'},
    {'Player': 'Sunil Narine', 'Team': 'KKR'},
    {'Player': 'Suyash Sharma', 'Team': 'KKR'},
    {'Player': 'Anukul Roy', 'Team': 'KKR'},
    {'Player': 'Andre Russell', 'Team': 'KKR'},
    {'Player': 'Venkatesh Iyer', 'Team': 'KKR'},
    {'Player': 'Harshit Rana', 'Team': 'KKR'},
    {'Player': 'Vaibhav Arora', 'Team': 'KKR'},
    {'Player': 'Varun Chakaravarthy', 'Team': 'KKR'},
    {'Player': 'KS Bharat', 'Team': 'KKR'},
    {'Player': 'Chetan Sakariya', 'Team': 'KKR'},
    {'Player': 'Mitchell Starc', 'Team': 'KKR'},
    {'Player': 'Angkrish Raghuvanshi', 'Team': 'KKR'},
    {'Player': 'Ramandeep Singh', 'Team': 'KKR'},
    {'Player': 'Sherfane Rutherford', 'Team': 'KKR'},
    {'Player': 'Manish Pandey', 'Team': 'KKR'},
    {'Player': 'Mujeeb Ur Rahman', 'Team': 'KKR'},
    {'Player': 'Gus Atkinson', 'Team': 'KKR'},
    {'Player': 'Sakib Hussain', 'Team': 'KKR'}
]

players=pd.DataFrame(players)

team_mapping = {'GT': 1, 'CSK': 2, 'LSG': 3, 'MI': 4, 'RR': 5, 'RCB': 6, 'KKR': 7, 'PBKS': 8, 'DC': 9, 'SRH': 10}

# Add team IDs based on the mapping
players['Team_ID'] = players['Team'].map(team_mapping)

# Sort the DataFrame by Team_ID
players = players.sort_values(by='Team_ID')

