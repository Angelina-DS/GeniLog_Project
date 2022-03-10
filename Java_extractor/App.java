package tablescraper;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class TableScraper {

public static void main(String[] args) {
    try {
        Document doc = Jsoup.connect("https://en.wikipedia.org/wiki/Comparison_of_digital_SLRs").get();
        Elements trs = doc.select("table.wikitable tr");

        //remove header row
        trs.remove(0);

        for (Element tr : trs) {

            Elements tds = tr.getElementsByTag("td.summary");
            Element td = tds.first();
            System.out.println("Episode: " + td.toString());
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
}

