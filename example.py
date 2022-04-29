from headloop import design

##Kroll et al 2021 eLife 10:e59683, https://doi.org/10.7554/eLife.59683
##Example from the paper: tbx16_AA

# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
#tbx16_AA_F  = st.text_input("Enter the fwd primer sequence", "Type Here ...")
#tbx16_AA_R  = st.text_input("Enter the rev primer sequence", "Type Here ...")
#tbx16_AA_guide  = st.text_input("Guide sequence and PAM, plus 15 bp downstream sequence", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
#if(st.button('Submit')):
	#result = name.title()
	#st.success(result)


#Forward primer
tbx16_AA_F = 'AGAGGGGGTGGGGCTTATAG'

#Reverse primer
tbx16_AA_R = 'CAGGGAAAGCCGTAGGTCTC'

#Guide sequence and PAM, plus 15 bp downstream sequence
tbx16_AA_guide = 'GGATATCCCAGCCGACCTGCGGCTCTGCTACAACGTGG'

#Orientation of guide with respect to forward primer: same strand = sense, opposite strand = 'antisense'
tbx16_AA_guide_orientation = 'antisense'

#Run the function
output = design(tbx16_AA_F, tbx16_AA_R, tbx16_AA_guide, tbx16_AA_guide_orientation)

#Output of the function: note that 'design' returns two primers as SeqRecord objects, with comments on how closely matched
#the predicated annealing temperatures are. Only one of those primers should be used, to be determined by testing.
#In this individual case, the antisense headloop primer was used for HL-PCR.
print(' Sense headloop primer:', output[0].seq, '\n', output[0].description, '\n', 
      'Antisense headloop primer:', output[1].seq, '\n', output[1].description)
print('success_repeat5')

#if(st.button('Submit')):
	#result = name.title()
	#st.success(result)
