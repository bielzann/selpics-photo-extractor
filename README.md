# 📷 selpics-photo-extractor

## What is Selpics?

<table>
  <tr>
    <td>
      <img src="https://github.com/bielzann/selpics-photo-extractor/assets/142922592/6c323211-a935-40b4-a837-bf7116900908" width="500")
    </td>
    <td align="justify">
      Selpics is a platform used by photographers to create albums and send them to clients for photo selection.
    </td>
  </tr>
</table>

## Gallery Summary
<table>
  <tr>
    <td align="justify">
      In the example screenshot, the photographer created an album with 33 photos and sent it to the client 'g173058@dac.unicamp.br', who selected the photos.
    </td>
    <td>
      <img src="https://github.com/bielzann/selpics-photo-extractor/assets/142922592/9e8c5f6c-21cc-4375-8c6d-89b30811ca48" width="1500">
    </td>
  </tr>
</table>

## Client Selection

<table>
  <tr>
    <td align="justify">
        <img src="https://github.com/bielzann/selpics-photo-extractor/assets/142922592/72fdc45a-4d02-4ce4-bbf1-48806c8bdd4a" width="500">
    </td>
    <td>
        In the client selection, the chosen photos appear with the same names as at the time of upload.
    </td>
  </tr>
</table>

## Extractor
<table>
  <tr>
    <td align="justify">
      The extractor opens the link provided in the 'Album URL', retrieves the names of the chosen photos, opens the selected directory in 'Photo directory', 
      copies and places them in a 'Chosen' folder within the root directory. The photographer must enter their Email and Password for everything to proceed correctly. 
      If everything goes well, in addition to the created folder, a list with the names of the chosen photos is displayed, along with a success message.
    </td>
  </tr>
</table>
<table>
  <tr>
    <td>
      <img src="https://github.com/bielzann/selpics-photo-extractor/assets/142922592/f6cb1154-4fee-40cc-906b-3f48afbd4d63" width="400">
    </td>
    <td>
      <img src="https://github.com/bielzann/selpics-photo-extractor/assets/142922592/a75f6254-0852-4d99-8cbf-1e54693de60c" width="550">
    </td>
  </tr>
</table>

### _Required 'pip install' commands_
<div style="border: 1px solid #000; padding: 10px;">
    <ul>
        <li>pip install selenium</li>
        <li>pip install beautifulsoup4</li>
        <li>pip install Pillow</li>
        <li>pip install tk</li>
        <li>pip install chromedriver-autoinstaller</li>
    </ul>
</div>
