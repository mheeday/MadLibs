import tkinter as tk

class MadLib:

    """ MADLIB Class containing methods for creating, starting and restarting thr GUI"""
    def __init__(self, root =tk.Tk(), headers=[]):
        self.root = root
        self.headers = headers
        self.root.title("MadLibs Generator")
        self.root.rowconfigure([0,1], minsize=30, weight=1) #setting minimum height of each row
        self.root.columnconfigure(0, minsize=70, weight=1) #setting minimum width of each column
        self.root.resizable(width=False, height=False) #Making sure the window isn't resizeable

        self.main_main = tk.Frame(self.root) # A main frame for the root
        self.main_main.pack()
        self.root_frame = tk.Frame(self.main_main) #A sub-frame for the headers
        self.root_frame.pack()

        self.row = 0
        self.font = 15
        for header in self.headers:
            tk.Label(self.root_frame, text=header, font=f"arial {self.font} bold").grid(row=self.row, column=0, sticky="nsew")
            self.row+=1
            if self.font > 10:
                self.font -=5
        
    def main_frame(self, sections={}):
        """ A sub frame for main frame which holds the sections a user can choose from"""
        self.sections = sections

        self.first_frame = tk.Frame(self.main_main)
        
        row = 0
        for section, func in self.sections.items():
            tk.Button(self.first_frame, text=section, font="arial 15 bold", bg="red", fg="white", command=func, width=23).grid(row=row, column=0,padx=5, pady=5)
            row+=1

    def start(self):
        """ Grids the application and run main loop"""
        self.root_frame.grid(row=0, column=0, sticky="nsew")
        self.first_frame.grid(row=1, column=0, sticky="nsew")
        self.root.mainloop()

    

    def restart(self):
        """ Destroys the current frame and returns to the main frame """
        self.next_frame.destroy()
        main = MadLib(headers=["Mad libs generator, have fun!", "Choose a category from below"])
        main.main_frame(sections={"The Photographer" :main.madlib1 , "The Butterfly" : main.madlib2})
        main.start()

    def sub_frame(self, header_text, requirements=[], column=3):
        """ A new instance for every button click; destroys the main frame and creates another based on the user's input"""
        self.header_text = header_text
        self.requirements = requirements

        self.main_main.destroy()
        self.next_frame = tk.Frame()
        self.next_frame.pack()
        self.next_frame.rowconfigure(list(range(len(requirements) + 1)), minsize=50, weight=1)
        self.next_frame.columnconfigure(list(range(column)), minsize=50, weight=1)
        tk.Button(self.next_frame, text="\N{LEFTWARDS BLACK ARROW}", command=main.restart).grid(row=0, column=0, sticky="nsew", padx=15, pady=15)
        tk.Label(self.next_frame, text=self.header_text, font=('calibre', 10, 'bold')).grid(row=0, column=1, columnspan=2, sticky="nsew")

        self.user_input = [] #for storing user's entry

        self.row = 1
        for item in self.requirements: #creating entries and labels based on the user's requirement
            self.column = 0
            self.i_label = item +"_label"
            self.i_entry = item +"_entry"
            self.i_label = tk.Label(self.next_frame, text=item, font=('calibre', 10, 'bold'))
            self.i_entry = tk.Entry(self.next_frame, font=('calibre', 10, 'bold'))
            self.user_input.append(self.i_entry)
            self.i_label.grid(row=self.row, column=self.column)
            self.i_entry.grid(row=self.row, column=self.column+1)
            self.row += 1
        
        if 'Photograph' in header_text:
            generate_btn = tk.Button(self.next_frame, text='Generate Madlib', command=main.output1)
            

        else:
            generate_btn = tk.Button(self.next_frame, text='Generate Madlib', command=main.output2)

        generate_btn.grid(row=(len(self.requirements) + 1), column=2, sticky="e", padx=10)

        self.output = tk.Label(self.next_frame, text="Result appear here")
        self.output.grid(row=(len(self.requirements) + 2), column=0, columnspan=3)


    def madlib1(self):
        """ Method that calls the first madlib i.e The photographer """

        self.main_main.destroy()
        main.sub_frame(column=3, header_text="Photograph Mad Libs\n Fill the form below", requirements=['Animal', 'Profession', 'Cloth', 'Thing', 'Name', 'Place', 'Verb', 'Food'])

    def output1(self):
        """  Parse the user's input and returns an output"""
        self.answer_list = []
        for word in self.user_input:
            self.answer_list.append(word.get())

        answer = 'Say ' + self.answer_list[7] + ', the photographer said as the camera flashed!\n ' + self.answer_list[4] + ' and I had gone to ' + self.answer_list[5] + ' to get our photos taken on my birthday\n. The first photo we really wanted was a picture of us dressed as ' + self.answer_list[0] + ' pretending to be a ' + self.answer_list[1] + '\n' + '. When we saw the second photo, it was exactly what I wanted. We both looked like ' + self.answer_list[3] + ' wearing ' + self.answer_list[2] + ' and ' + self.answer_list[6] + '\n --exactly what I had in mind'
        self.output['text'] = answer

    def madlib2(self):
        """ Method that calls the second madlib i.e Apple and Apple Story """
        self.main_main.destroy()
        main.sub_frame(column=3, header_text="Apple and Apple Mad Lib\n Fill the form below", requirements=['Person', 'Color', 'Foods', 'Adjective', 'Thing', 'Place', 'Verb', 'Adverb', 'Food', 'Things'])

    def output2(self):
        """  Parse the user's input and returns an output"""
        self.answer_list = []
        for word in self.user_input:
            self.answer_list.append(word.get())

        answer = 'Today, we picked apple from '+ self.answer_list[0]+ "'s Orchard\n. I had no idea there were so many different varieties of apples\n. I ate " + self.answer_list[1] + ' apples straight off the tree that tested like '+self.answer_list[2]+ '.\n Then there was a '+ self.answer_list[3] + ' apple that looked like a ' + self.answer_list[4] + '\n.When our bag were full, we went on a free hay ride to '+ self.answer_list[5] + ' and back. \nIt ended at a hay pile where we got to ' + self.answer_list[6] + ' ' + self.answer_list[7] + '. \nI can hardly wait to get home and cook with the apples. \nWe are going to make appple ' +self.answer_list[8]+ ' and '+ self.answer_list[9] +' pies!.'
        self.output['text'] = answer
        


main = MadLib(headers=["Mad libs generator, have fun!", "Choose a category from below"])
main.main_frame(sections={"The Photographer" :main.madlib1 , "The Butterfly" : main.madlib2})
main.start()