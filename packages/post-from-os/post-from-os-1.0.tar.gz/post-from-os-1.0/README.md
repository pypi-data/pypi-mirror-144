# Post Events From Opensea

#### This is a package for the sales bots. Below you can find a few examples. Only Twitter is supported currently. Please check out the GitHub for more details.

### Example Code 1
    from post_from_os.post_to_twitter_obj import ManageFlowObj
    
    ManageFlowObj('example_file.txt')  # does not print out rare traits in caption

### Example Code 2
    from post_from_os.post_to_twitter_obj import ManageFlowObj
    
    ManageFlowObj('example_file.txt', True)  # prints out rare traits in caption
    
### How example_file.txt _MUST_ look
    Hashtags
    CollectionSlug
    TwitterAPIKey
    TwitterAPIKeySecret
    TwitterAccessToken
    TwitterAccessTokenSecret
    OpenseaAPIKey
    EtherscanAPIKey (OPTIONAL: PictureName)

### Example file 1
    #hashtagone #hashtagtwo #hashtagthree ...
    boredapeyachtclub
    oeir23o4ij2oikew
    oweri23-492o3k4l2
    o23i495020dm25
    23oi4m2moi2eiok2o
    430r9fjdsifdklsf
    2omm4o234i23m4204940 BoredApe

### Example file 2
    #hashtagone #hashtagtwo ...
    boredapeyachtclub
    oeir23o4ij2oikew
    oweri23-492o3k4l2
    o23i495020dm25
    23oi4m2moi2eiok2o
    430r9fjdsifdklsf
    2omm4o234i23m4204940