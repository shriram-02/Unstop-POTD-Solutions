
import java.io.*;
import java.util.*;

public class Main {

    static class Batch {
        long id;
        long lastDay;
        long remaining;
        boolean active;

        Batch(long id, long lastDay, long remaining) {
            this.id = id;
            this.lastDay = lastDay;
            this.remaining = remaining;
            this.active = true;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        int Q = Integer.parseInt(br.readLine().trim());

        PriorityQueue<Batch> pq = new PriorityQueue<>(
            (a, b) -> {
                if (a.lastDay != b.lastDay) {
                    return Long.compare(a.lastDay, b.lastDay);
                }
                return Long.compare(a.id, b.id);
            }
        );

        HashMap<Long, Batch> map = new HashMap<>();

        long wasted = 0;

        StringBuilder output = new StringBuilder();

        for (int i = 0; i < Q; i++) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            String type = st.nextToken();

            if (type.equals("R")) {

                long id = Long.parseLong(st.nextToken());
                long lastDay = Long.parseLong(st.nextToken());
                long doses = Long.parseLong(st.nextToken());

                Batch batch = new Batch(id, lastDay, doses);

                pq.offer(batch);
                map.put(id, batch);

            }

            else if (type.equals("C")) {

                long id = Long.parseLong(st.nextToken());

                Batch batch = map.get(id);

                if (batch != null && batch.active) {
                    batch.active = false;
                    batch.remaining = 0;
                }

            }

            else if (type.equals("I")) {

                long day = Long.parseLong(st.nextToken());
                long required = Long.parseLong(st.nextToken());

                long supplied = 0;

                // Remove expired, recalled and exhausted batches.
                while (!pq.isEmpty()) {

                    Batch batch = pq.peek();

                    // Remove recalled or exhausted batches.
                    if (!batch.active || batch.remaining == 0) {
                        pq.poll();
                        continue;
                    }

                    // Expired batches must be discarded.
                    if (batch.lastDay < day) {

                        pq.poll();

                        wasted += batch.remaining;

                        batch.remaining = 0;
                        batch.active = false;

                        continue;
                    }

                    // The earliest batch is still usable.
                    break;
                }

                // Fulfil the request using earliest-expiring batches.
                while (required > 0 && !pq.isEmpty()) {

                    Batch batch = pq.peek();

                    if (!batch.active || batch.remaining == 0) {
                        pq.poll();
                        continue;
                    }

                    long take = Math.min(required, batch.remaining);

                    supplied += take;
                    required -= take;
                    batch.remaining -= take;

                    if (batch.remaining == 0) {
                        batch.active = false;
                        pq.poll();
                    }
                }

                long shortage = required;

                output.append(supplied)
                      .append(" ")
                      .append(shortage)
                      .append("\n");
            }
        }

        output.append("wasted ").append(wasted);

        System.out.print(output);
    }
}