# LivePeerSDK
## Make LivePeerAPICalls from Python
## License : MIT
#####
##### Copyright (c) 2022 RAGAVENDIRAN BALASUBRAMANIAN. 
##### GMAIL   : bgragavendiran@gmail.com
##### LINKEDIN: https://www.linkedin.com/in/ragavendiranbalasubramanian/
#####
> Permission is hereby granted, free of charge, to any person obtaining a copy
> Of this software and associated documentation files (the "software"), to deal
> In the software without restriction, including without limitation the rights
> To use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> Copies of the software, and to permit persons to whom the software is
> Furnished to do so, subject to the following condition that the owner and source contributors names and 
> details  shall not to be removed from the project
> 
> ###### 
>  The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> ###### 
>  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>  SOFTWARE.
## Powered By
[![N|Solid](https://images.squarespace-cdn.com/content/v1/54dab2c9e4b0512a94d54e0d/1514399509872-CKQEQL1C7O05DT70HWZC/LivepeerBrand_BradleyRHughes_Slide_02.jpg)](https://www.linkedin.com/in/ragavendiranbalasubramanian/)


![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

LivePeerSDK for Python Developed by Team Heptre,
is a realtime PythonSDK that directly interlinks with the LivePeerAPI 
endpoints which makes the life of the user simple.


## Features

- simply start and use livepeer with ``` livePeer=LivePeerSDK(<LIVEPEER_API_KEY>)  ```      
- The Library is highly modular and plug and play in nature
- Forget handling requests just make the function call.
- The request responses are all dicts 
- Detailed Docs Feeling Stuck Anywhere?? help(<functionName>) will get you right back on track.

## Installation

LivePeerSDK requires [python3](https://www.python.org/downloads/) to run.

```sh
pip install LivePeerSDK_Python
```

## EXAMPLES
Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.
```
from LivePeerSDK_Python import LivePeerSDK
LivePeer=LivePeerSDK(str(<YOUR_LIVEPEER_API_KEY>))

for asset in LivePeer.listAssets():
    print(asset["id"])

OUTPUT:
19233508-5a34-4508-b54f-fe71b062d225
21bd42e3-044e-4093-b920-46fc104b395e
67095c2f-beda-47f1-ad04-2787fad529c9
aecfa170-7d50-4e47-93aa-f0cae8912398
a20373cd-5c27-4948-a5cb-bb55de5def70
d8b52bb6-4bda-4059-bd73-e6dae2d88c80
b9ea232c-6b6c-4a36-9a9c-809f2144592f

Process finished with exit code 0
```
## USAGE


| Function | USAGE |
| ------ | ------ |
| createUploadUrl(`name`) | Creates a new upload url to directly upload a video asset to livepeer |
| exportAssetToIPFS(`assetID`)| Export a specific `assetID` to ipfs it initializes a cloud async call in livepeer which creates a respective `taskID` |
| importWebAsset(`url`, `name`) | Import a video Asset to Livepeer from an external URL.|
|listAssets() | List all assets currently uploaded to livepeer in the form of a dictionary |
|listTasks()|List all tasks currently uploaded to livepeer |
|retrieveAsset(`assetID`)|Retrieve a specific `assetId` from live peer|
|retrieveTask(`taskID`)|Retrieve a specific `taskId` from livepeer with ipfs link|
|uploadContent(`filePATH`, `assetURL`)|Create a new Direct Upload URL  to directly upload a video Asset to Livepeer|
_______________
> ## createUploadUrl(`name`)
>:parameter
>"name":"Example name"
>
>:returns
>dict
>{
> url:<URL>,
> asset:{'id':<assetid>, 'playbackId':<playbackId>, 'userId':<userId>, 'createdAt':<timestamp>, >'status':<STATUS>, 'name':<name>}
> task:{'id':<taskid>, 'createdAt':<timestamp>, 'type':<importType>, 'outputAssetId':<outassetid>, >'userId':<uid>, 'params':{'uploadedObjectKey': <type>}}, 'status':{'phase': <STATUS>, 'updatedAt': <>timestamp>}}
>}
_________________
> ## exportAssetToIPFS(`assetID`)
>:param
> "assetID":"$AssetID"
> 
> :returns
> {}
_______________
> ## importWebAsset(`url`, `name`)
>:param
>        "url":"$EXTERNAL_URL",
>        "name":"Example name\"
_______________
> ## listAssets()
>:param : NONE
> :returns
> <class 'list'>
> LIST OF DICTIONARIES OF FORMAT  [<class 'dict>,...]
>
> FOR UPLOADED VIDEOS
> {
> id : <`assetID`>,
> hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
> name : <name>,
> size : <size>,
> status : ready,
> userId : <userID>,
> createdAt : <timestamps>,
> updatedAt : <timestamps>,
> videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
> playbackId : <playbackID>,
> downloadUrl : <downloadURLfromLIVEPEERCDN>
> }
>
> FOR PENDING VIDEOS
> {
> 'id': <ID>,
> 'name':  <name>,
> 'status': 'waiting',
> 'userId': <userID>,
> 'createdAt': <timestamps>,
> 'playbackId': <playbackID>,
> }
>_______________
> ## listTasks()
_______________
>:param : NONE
>
>:returns
><class 'list'>
>LIST OF DICTIONARIES OF FORMAT
>
>FOR EXPORT
>{
>'id':<taskID>,
>'type':<type>,
>'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
>}
>
>FOR IMPORT
>{
>'id': <taskID>,
>'type': 'import',
>'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
>'name': <name>,
>'size': <size>,
>'type': 'video',
>'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
>}}},
>'params': {'import': {'uploadedObjectKey': <uploadKey>}},
>'status': {
>'phase': <status>,
>'userId' : <userID>,
>'createdAt': <timestamps>,
>'updatedAt' : <timestamps>,
>'outputAssetId': <outputassetID>
>}
>}     
>_____________
> ## retrieveAsset(`assetID`)
>:param :
> `assetID` obtained from createUploadURL(name)
> :returns
> <class 'dict'>
> LIST OF DICTIONARY OF FORMAT
>
> FOR UPLOADED VIDEOS
> {
> id : <`assetID`>,
> hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
> name : <name>,
> size : <size>,
> status : ready,
> userId : <userID>,
> createdAt : <timestamps>,
> updatedAt : <timestamps>,
> videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
> playbackId : <playbackID>,
> downloadUrl : <downloadURLfromLIVEPEERCDN>
> }
>
> FOR PENDING VIDEOS
> {
> 'id': <ID>,
> 'name':  <name>,
> 'status': 'waiting',
> 'userId': <userID>,
> 'createdAt': <timestamps>,
> 'playbackId': <playbackID>,
> }
>_______________
> ## retrieveTask(`taskID`)
>:param : 
>"taskID obtained from listTASKS
>
>:returns
><class 'dict'>
>LIST OF DICTIONARIES OF FORMAT
>
>FOR EXPORT
>{
>'id':<taskID>,
>'type':<type>,
>'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
>}
>
>FOR IMPORT
>{
>'id': <taskID>,
>'type': 'import',
>'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
>'name': <name>,
>'size': <size>,
>'type': 'video',
>'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
>}}},
>'params': {'import': {'uploadedObjectKey': <uploadKey>}},
>'status': {
>'phase': <status>,
>'userId' : <userID>,
>'createdAt': <timestamps>,
>'updatedAt' : <timestamps>,
>'outputAssetId': <outputassetID>
>}
>}     
>_____________
> ## uploadContent(`filePATH`, `assetURL`)
>:param
>"filePATH":"PASS THE FILE PATH OF VIDEO IN H264 and AAC codec
>"assetURL":ASSET URL FOR THE FILE
>
>:returns
>{}
>_____________


