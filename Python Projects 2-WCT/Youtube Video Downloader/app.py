from pytube import YouTube

link=""

YouTube_1=YouTube(link)

#print(YouTube_1.title)
#print(YouTube_1.thumbnail_url)

#for all formats
videos=YouTube_1.streams.all()  

#only audio
#videos=YouTube_1.streams.filter(only_audio=True)

vid=list(enumerate(videos))
for i in vid:
    print(i)

strm=int(input("Enter: "))
videos[strm].download()
print("Successful")

'''
# Install virtualenv if you don't have it
sudo apt install python3-virtualenv

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Now you can install pytube using pip without sudo
pip install pytube

# When you're done, deactivate the virtual environment
deactivate

'''