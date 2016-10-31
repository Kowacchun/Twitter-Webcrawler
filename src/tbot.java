import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

public class TBot
{
	//TwitterException occurs when something fucks up
	public static void main(String[] args) throws TwitterException
	{
		//begin base code below

		TwitterStream twitterStream = new TwitterStreamFactory(config).getInstance();
		StatusListener listener = new StatusListener()
		{

			@Override

			public void onStatus(Status status)
			{
				System.out.println("@" + status.getUser().getScreenName() + " - " + status.getText());
			}

			@Override
			public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice)
			{
				System.out.println("Status deletion Notice ID: " + statusDeletionNotice.getStatusId());
			}

			@Override
			public void onTrackLimitationNotice(int numberOfLimitedStatuses)
			{
				System.out.println("Track Limitation Notice: " + numberOfLimitedStatuses);
			}

			@Override
			public void onScrubGeo(long userId, long upToStatusId)
			{
				System.out.println("Scrub_Geo Event User ID:" + userId + " upToStatusId:" + upToStatusId);
			}

			@Override
			public void onStallWarning(StallWarning warning)
			{
				System.out.println("Stall Warning: " + warning);
			}

			@Override
			public void onException(Exception e)
			{
				e.printStackTrace();
			}
		};

		twitterStream.addListener(listener);
		twitterStream.sample();
	}
}
