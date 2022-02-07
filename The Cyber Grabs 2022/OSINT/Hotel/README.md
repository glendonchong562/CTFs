# Hotel (100 points)

## Challenge Description: Some answers are hidden in the details, Find the hotel from where this image was uploaded. 

This challenge involves a picture file called [hotel.jpg](./hotel.jpg). The challenge description was a giveaway that details can be found in the metadata of the image. Running *exiftool*, I find the latitude and longitude of the photo location: 

![exif_hotel](https://user-images.githubusercontent.com/71312079/152739315-cc3c4aba-3ea9-43b7-86a9-982c99f76772.png)

I next go to Google Maps and input these coordinates, which reveal that the location is a hotel in Amsterdam called the **Leonardo Hotel**.

![leonardo](https://user-images.githubusercontent.com/71312079/152739301-a3879a35-29ff-4d6c-9619-c99ac7aea715.png)


FLAG: `flag{leonardo}`