import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

public class TBot
{
	//TwitterException occurs when something fucks up
	public static void main(String... args) throws TwitterException
	{
		//begin base code below

		TwitterStream twitterStream = new TwitterStreamFactory(config).getInstance();
		TweetListener listener = new TweetListener();
		twitterStream.addListener(listener);


	}
}
