class Solution {
    public String solution(String new_id) {
        String str1 = new_id.toLowerCase();
        String str2 = str1.replaceAll("[^[a-z][0-9]-_.]", "");
        String str3 = str2.replaceAll("\\.{2,}", ".");
        String str4 = str3.replaceAll("^\\.|\\.$", "");
        String str5 = str4.isEmpty() ? "a" : str4;
        String str6 = str5.length() > 15 ? str5.substring(0, 15) : str5;
        str6 = str6.replaceAll("\\.$", "");
        String str7 = str6;
        String s = "" + str7.charAt(str7.length() - 1);
        while (str7.length() < 3){
            str7 += s;
        }
        return str7;
    }
}