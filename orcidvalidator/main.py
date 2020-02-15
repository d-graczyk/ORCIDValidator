"""
ORCIDValidator

A tiny tkinter-based tool to validate an ORCID ID length and its checksum.

Version: 0.1 (February 2020)

Author: d-graczyk

"""

import sys
import os
from tkinter import font
import tkinter as tk
from orcidvalidator.orcid_misc import check_orcid_id_checksum

# This bit is required for proper embedding of the image file and getting
# an access to it when the application is launched from one-file bundle executable.
if getattr(sys, 'frozen', False):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    path_to_the_img = os.path.join(base_path, 'window.ico')
else:
    path_to_the_img = os.path.join(os.getcwd(), 'icon/window.ico')


class MainApplication:
    def __init__(self, parent):

        self.master_frame = tk.Frame(parent)
        self.master_frame.pack()

        self.parent = parent
        self.parent.title('ORCID ID Validator')
        self.parent.geometry("310x98")
        self.parent.minsize(width=310, height=98)

        if os.path.isfile(path_to_the_img):
            self.parent.iconbitmap(path_to_the_img)

        self.border_width = 0

        self.window_font = font.Font(family="Arial", size=11)
        self.status_font = font.Font(family="Arial", size=10)

        self.frm_top_row = tk.Frame(master=self.master_frame,
                                    relief=tk.RAISED,
                                    borderwidth=self.border_width, padx=3, pady=3)
        self.frm_top_row.grid(row=1, column=1, sticky=tk.EW)

        self.label_1 = tk.Label(master=self.frm_top_row, font=self.window_font, text="Enter ORCID ID:")
        self.label_1.grid(row=1, column=1, sticky=tk.W)

        self.ent_orcid_id = tk.Entry(master=self.frm_top_row, width=19, font=self.window_font)
        self.ent_orcid_id.focus()
        self.ent_orcid_id.bind("<Return>", self.validate_orcid)
        self.ent_orcid_id.grid(row=1, column=2, sticky=tk.E)

        self.frm_middle_row = tk.Frame(master=self.master_frame,
                                       relief=tk.RAISED,
                                       borderwidth=self.border_width, padx=3, pady=3)
        self.frm_middle_row.grid(row=2, column=1)

        btn_validate = tk.Button(master=self.frm_middle_row,
                                 text='Verify',
                                 width=14, height=1,
                                 font=self.window_font,
                                 command=self.validate_orcid)
        btn_validate.grid()

        self.frm_bottom_row = tk.Frame(master=self.master_frame,
                                       relief=tk.RAISED,
                                       borderwidth=self.border_width, )
        self.frm_bottom_row.grid(row=3, column=1)

        self.label_2 = tk.Label(master=self.frm_bottom_row, font=self.window_font, text="Status:")
        self.label_2.grid(row=1, column=1, sticky=tk.W)

        self.frm_status = tk.Frame(master=self.frm_bottom_row,
                                   relief=tk.SUNKEN,
                                   borderwidth=1,
                                   width=224,
                                   height=24,
                                   padx=0, pady=0)
        self.frm_status.grid_propagate(False)
        self.frm_status.grid(row=1, column=2)

        self.lbl_status = tk.Label(master=self.frm_status,
                                   font=self.status_font, text="Welcome. Enter ORCID ID.")
        self.lbl_status.grid(row=1, column=1, sticky=tk.W)

    def set_status(self, status_msg, status_color='black'):
        self.lbl_status.config(text=status_msg, fg=status_color)

    def validate_orcid(self):
        orcid_id_str = self.ent_orcid_id.get()
        orcid_id_str_len = len(orcid_id_str)

        if orcid_id_str_len == 0:
            self.set_status('Enter ORCID ID.', 'red')
        elif orcid_id_str_len != 19:
            self.set_status('ID is NOT valid! (invalid length)', 'red')
        else:
            validation_result = check_orcid_id_checksum(orcid_id_str)

            if validation_result:
                self.set_status('ID is valid.', 'green')
            else:
                self.set_status('ID is NOT valid! (invalid checksum)', 'red')


if __name__ == "__main__":
    root = tk.Tk()
    _ = MainApplication(root)
    root.mainloop()
