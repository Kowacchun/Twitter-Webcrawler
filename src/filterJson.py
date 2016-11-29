import json

print "Filtering JSON Fields...."

with open("10312016tweets.json") as infile:

    jsonSize = 500

    outFileSize = 0
    outFileCount = 1

    for line in infile:
    	parsed_json = json.loads(line)

        if 'created_at' not in parsed_json:
            creationDate = "None"
        else:
            creationDate = parsed_json['created_at']

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if 'id' not in parsed_json:
            tweetID = "None"
        else:
            tweetID = parsed_json['id']
            
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if 'id_str' not in parsed_json:
            str_tweetID = "None"
        else:
            str_tweetID = parsed_json['id_str']

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        if 'text' not in parsed_json:
            tweetContent = "None"
        else:
            tweetContent = parsed_json['text'] 

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
        if 'source' not in parsed_json:
            tweetSource = "None"
        else:
            tweetSource = parsed_json['source']

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        if 'user' not in parsed_json:

            print str_tweetID
            outFileName = "FilteredHalloweenTweets" + str(outFileCount) + ".json"

            with open(outFileName, "a") as outfile:
                outfile.write("{}\n".format(json.dumps({'created_at':creationDate, 'id':tweetID, 'id_str':str_tweetID, 'text':tweetContent, 'source':tweetSource, 'user':"None"})))
                outFileSize = outFileSize + jsonSize

                if outFileSize == 10000000:
                    outFileSize = 0
                    outFileCount = outFileCount + 1
                    print "New File Created"
                    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        else:
            print str_tweetID
            outFileName = "FilteredHalloweenTweets" + str(outFileCount) + ".json"

            if 'id' not in parsed_json['user']:
                userID = "None"
            else:
                userID = parsed_json['user']['id']

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            if 'id_str' not in parsed_json['user']:
                str_userID = "None"
            else:
                str_userID = parsed_json['user']['id_str']

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            if 'name' not in parsed_json['user']:
                userName = "None"
            else:
                userName = parsed_json['user']['name']

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            if 'screen_name' not in parsed_json['user']:
                userScreenName = "None"
            else:
                userScreenName = parsed_json['user']['screen_name']

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            if 'url' not in parsed_json['user']:
                userURL = "None"
            else:
                userURL = parsed_json['user']['url']

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        	with open(outFileName, "a") as outfile:
        		outfile.write("{}\n".format(json.dumps({'created_at':creationDate, 'id':tweetID, 'id_str':str_tweetID, 'text':tweetContent, 'source':tweetSource, 'user':{'id':userID, 'id_str':str_userID, 'name':userName, 'screen_name':userScreenName, 'url':userURL}})))
                outFileSize = outFileSize + jsonSize

                if outFileSize == 10000000:
                    outFileSize = 0
                    outFileCount = outFileCount + 1
                    print "New File Created"
                    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print "Filtering complete!"

