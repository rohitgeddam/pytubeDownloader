import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlTextArea
from   pyforms.controls import ControlLabel

from pytube import YouTube

from databaseConnection import Base, engine,Session
from downloadedModel import Downloaded

Base.metadata.create_all(engine)
session = Session()

class youPyDownloader(BaseWidget):

    def __init__(self):
        super(youPyDownloader,self).__init__('youtube downloader')

        #definatino of forms fields
        self._videoUrl = ControlText('Video Url')
        self._button = ControlButton('View Details')
        self._details = ControlTextArea("Details")
        self._downloadButton = ControlButton("Download")

        self._downloadCompleted = ControlLabel(" ")


        self._button.value = self.__buttonAction
        self._downloadButton.value = self.__downloadAction


        self.formset = [ ('_videoUrl'), '_button', '_details', '_downloadButton' ,'_downloadCompleted']
        #The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        #If you remove the ' ' the forms will occupy the entire window
        self.mainmenu = [
        { 'File': [
                {"Downloaded Files": self.__viewDownloaded},
                {'About': self.__about},
                '-',
                {'Quit': self.__quit}
            ]
        }
       
    ]
    def __viewDownloaded(self):
        ...

    def __about(self):
        ...
    def __quit(self):
        ...

    def __downloadAction(self):
        yt = self.__getDetails()
        stream = yt.streams.filter(progressive = True).first()
        stream.download()
        video = Downloaded(yt.title)
        print("downloaded - " + yt.title)
        session.add(video)
        session.commit()
        session.close()
        self._downloadCompleted.value = "Download Completed!!"
        print("Download completed!!")

    def __buttonAction(self):
       

        yt = self.__getDetails()
        print(self._videoUrl.value)
        self._details.value =  "\nVideo title - "+ yt.title


    def __getDetails(self):
       self._downloadCompleted.value = " "   
       yt = YouTube(self._videoUrl.value)
    #    print(yt.title)
       return yt



if __name__ == "__main__":
    pyforms.start_app(youPyDownloader)