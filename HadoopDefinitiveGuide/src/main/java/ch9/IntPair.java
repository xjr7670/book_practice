package ch9;

import org.apache.hadoop.io.WritableComparable;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;


public class IntPair implements WritableComparable<IntPair> {
    
    int first;
    int second;

    public IntPair() {}

    public IntPair(int first, int second) {
        super();
        this.first = first;
        this.second = second;
    }

    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(first);
        out.writeInt(second);
    }

    @Override
    public void readFields(DataInput in) throws IOException {
        first = in.readInt();
        second = in.readInt();
    }

    @Override
    public int compareTo(IntPair pair) {
        int cmpFirst = Integer.valueOf(first).compareTo(pair.first);
        if (cmpFirst != 0) {
            return cmpFirst;
        } else {
            return Integer.valueOf(second).compareTo(pair.second);
        }
    }

    @Override
    public int hashCode() {
        return first * 163 + second;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof IntPair) {
            IntPair ip = (IntPair) obj;
            return first == ip.getFirst() && second == ip.getSecond();
        }
        return false;
    }

    public int getFirst() {
        return first;
    }

    public int getSecond() {
        return second;
    }

    @Override
    public String toString() {
        return first + "\t" + second;
    }

    public static int compare(int first1, int first2) {
        return Integer.valueOf(first1).compareTo(first2);
    }
}
