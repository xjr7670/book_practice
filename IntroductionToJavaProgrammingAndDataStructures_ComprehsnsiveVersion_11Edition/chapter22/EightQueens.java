import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;

public class EightQueens extends Application {
    // 象棋盘的规格
    public static final int SIZE = 8;
    //  皇后被放置在 (i, queens[i])
    // -1 表示当前没有皇后被放置在第 i 行
    // 初始状态下，把皇后放在第 0 行的 (0, 0)
    private int[] queens = { -1, -1, -1, -1, -1, -1, -1, -1 };

    // 重写 Application 类中的 start 方法
    @Override
    public void start(Stage primaryStage) {
        search(); // 搜索方案

        // 显示象棋盘
        GridPane chessBoard = new GridPane();
        chessBoard.setAlignment(Pos.CENTER);
        Label[][] labels = new Label[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                chessBoard.add(labels[i][j] = new Label(), j, i);
                labels[i][j].setStyle("-fx-border-color: black");
                labels[i][j].setPrefSize(55, 55);
            }
        }

        // 显示皇后
        Image image = new Image("queen.jpg");
        for (int i = 0; i < SIZE; i++) {
            labels[i][queens[i]].setGraphic(new ImageView(image));
        }

        // 创建一个 scene 并放在 stage 中
        Scene scene = new Scene(chessBoard, 55 * SIZE, 55 * SIZE);
        primaryStage.setTitle("EightQueens"); // 设置 stage 的标题
        primaryStage.setScene(scene); // 放置 scene 到 stage
        primaryStage.show(); // 显示 stage
    }
    
    /** 搜索方案 */
    private boolean search() {
        // k - 1 表示目前已经放置的皇后数量
        // 我们正在查找在第 k 行放置皇后的位置
        int k = 0;
        while (k >= 0 && k < SIZE) {
            // 查找一个位置在第 k 行放置皇后
            int j = findPosition(k);
            if (j < 0) {
                queens[k] = -1;
                k--; // 回溯到上一行
            } else {
                queens[k] = j;
                k++;
            }
        }

        if (k == -1) {
            return false; // 没有解决方案
        } else {
            return true; // 找到了一个方案
        }
    }
    
    public int findPosition(int k) {
        int start = queens[k] + 1; // 搜索一个新位置

        for (int j = start; j < SIZE; j++) {
            if (isValid(k, j)) {
                return j; // (k, j) 是当前可以放置皇后的位置
            }
        }

        return -1;
    }
    
    /** 如果皇后能够被放置在 (row, column) 的话，就返回 true */
    public boolean isValid(int row, int column) {
        for (int i = 1; i <= row; i++) {
            if(queens[row - i] == column   // 检查列
                || queens[row - i] == column - i    // 检查左上方格子
                || queens[row -i] == column + i) {   // 检查右上方格子 
                    return false;   // 有冲突
            }
        }

        return true;    // 没有冲突
    }
}