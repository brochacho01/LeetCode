import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;

public class compStrings {
    public static void main(String[] args) throws IOException {
        // String[] strings = {
        //         "}81a35847155f37671400399b56515258074d41898959a41503c51345709164f21005007d91f44817335458257293959e45{95:97G03A96L01F70",
        //         "}64a82819165f95695445383b10593296025d40874951a88500c35303740197f11079051d76f98824319437253272976e61{77:43G30A42L71F35",
        //         "}34a42890172f81603444332b14599206075d13827998a83578c59330702142f38009065d05f00871385494252286916e11{64:09G51A60L88F63",
        //         "}63a79851138f13633447310b63572264036d39860932a07552c42317744110f98049057d52f60858352466239250927e43{79:96G62A33L50F47",
        //         "}08a13870159f04660460381b16577269084d65875976a56587c43362755118f80071021d23f97819387464255270915e13{15:60G35A84L07F61",
        //         "}28a17860113f08632428369b22586251093d34800988a88581c13331786113f40089085d09f08827397462230261929e21{36:50G59A70L14F34",
        //         "}75a42890199f72677497398b28566253012d75891933a44528c39366770122f58006013d03f71861380446256269918e11{95:21G99A41L81F79",
        //         "}65a67863156f08647444311b54500217083d92840905a84534c76309723125f18075061d77f53886305460252203914e74{77:99G48A42L87F16",
        //         "}51a74897100f43643476347b70520228071d20848912a73569c89308730186f88065083d24f90857390431210249905e25{22:10G38A28L23F21",
        //         "}21a32888137f57693453356b98574246021d02813973a30598c46329767159f55037043d37f45883399463254293957e53{50:46G01A54L54F70" };
        String[] strings = {
        "}00964017c25d32e53288a67267281162d95582574e58556e55f06885600e79452243e73958016490458506646950804752{85:18G43A24L66F29",
        "}66973087c15d74e35247a41244224109d10589588e92571e71f18835636e51468259e71948078400472573659936897724{32:46G66A74L87F43",        
        "}92946005c29d24e76219a08243288141d47559514e35509e36f85815627e88431221e36927082453492507684949851795{21:13G77A07L93F65",
        "}10951010c10d85e92244a34233258163d94505501e37576e81f09886694e39476217e54942057484420576696911848776{75:18G92A96L36F77",
        "}47910079c36d39e16290a43282291178d82580513e60564e80f74887667e70411239e60924024459451556689916893712{20:62G22A63L72F12",
        };
        comp(strings);
    }

    public static void comp(String[] tokens) throws IOException {
        int len = tokens[0].length();
        char[] result = new char[len];
        Arrays.fill(result, '@');
        HashMap<Character, Integer> chars = new HashMap<Character, Integer>();
        for (int i = 0; i < len; i++) {
            char c = tokens[0].charAt(i);
            int flag = 0;
            for (int j = 0; j < tokens.length; j++) {
                if(tokens[j].charAt(i) != c){
                    flag = 1;
                }
                // if (chars.containsKey(tokens[j].charAt(i))) {
                //     result[i] = tokens[j].charAt(i);
                // } else {
                //     chars.put(tokens[j].charAt(i), 1);
                // }
            }
            if(flag == 0){
                result[i] = c;
                System.out.print(c);
            }
            chars.clear();
        }
        System.out.println();
        for (int i = 0; i < len; i++) {
            System.out.print(result[i]);
        }
    }
}
