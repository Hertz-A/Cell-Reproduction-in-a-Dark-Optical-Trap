import cv2
import pandas as pd
from tqdm import tqdm

def gerar_video_com_rastro(video_path, df, output_path):
    vidcap = cv2.VideoCapture(video_path)
    
    frame_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    pontos_acumulados = []

    with tqdm(total=total_frames, desc="Processando vídeo", unit="frame") as pbar:
        while True:
            ret, frame = vidcap.read()
            if not ret:
                break
            
            frame_atual = int(vidcap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
            pontos_novos = df[df["Frame"] == frame_atual][["Centro_X", "Centro_Y"]].values

            for x, y in pontos_novos:
                pontos_acumulados.append((int(x), int(y)))

            for x, y in pontos_acumulados:
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

            out.write(frame)
            pbar.update(1)

    # Libera os recursos
    vidcap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"\nVídeo salvo em: {output_path}")

csv_path_1 = r"C:\Users\PUC\Desktop\yolo\sol7 - v1 - yolo.csv"
csv_path_2 = r"C:\Users\PUC\Desktop\yolo\sol7 - v2 - yolo.csv"
csv_path_3 = r"C:\Users\PUC\Desktop\yolo\sol7 - v3 - yolo.csv"
csv_path_4 = r"C:\Users\PUC\Desktop\yolo\sol7 - v4 - yolo.csv"
csv_path_5 = r"C:\Users\PUC\Desktop\yolo\sol7 - v5 - yolo.csv"
csv_path_6 = r"C:\Users\PUC\Desktop\yolo\sol7 - v6 - yolo.csv"
csv_path_7 = r"C:\Users\PUC\Desktop\yolo\sol7 - v7 - yolo.csv"
csv_path_8 = r"C:\Users\PUC\Desktop\yolo\sol7 - v8 - yolo.csv"

df_1 = pd.read_csv(csv_path_1, encoding='cp1252')
df_2 = pd.read_csv(csv_path_2, encoding='cp1252')
df_3 = pd.read_csv(csv_path_3, encoding='cp1252')
df_4 = pd.read_csv(csv_path_4, encoding='cp1252')
df_5 = pd.read_csv(csv_path_5, encoding='cp1252')
df_6 = pd.read_csv(csv_path_6, encoding='cp1252')
df_7 = pd.read_csv(csv_path_7, encoding='cp1252')
df_8 = pd.read_csv(csv_path_8, encoding='cp1252')

df_1 = df_1.loc[df_1["Centro_X"] >= 800]
df_1 = df_1.loc[df_1["Centro_X"] <= 1100]
df_1 = df_1.loc[df_1["Centro_Y"] <= 500]
df_1 = df_1.loc[df_1["Confiança"] > 0.7]

df_2 = df_2.loc[df_2["Centro_X"] >= 800]
df_2 = df_2.loc[df_2["Centro_X"] <= 1100]
df_2 = df_2.loc[df_2["Centro_Y"] <= 500]
df_2 = df_2.loc[df_2["Confiança"] > 0.7]

df_3 = df_3.loc[df_3["Centro_X"] >= 900]
df_3 = df_3.loc[df_3["Centro_X"] <= 1150]
df_3 = df_3.loc[df_3["Centro_Y"] >= 400]

df_4 = df_4.loc[df_4["Centro_X"] <= 1050]
df_4 = df_4.loc[df_4["Centro_X"] >= 900]
df_4 = df_4.loc[df_4["Centro_Y"] <= 550]
df_4 = df_4.loc[df_4["Confiança"] > 0.7]

df_5 = df_5.loc[df_5["Centro_X"] >= 800]
df_5 = df_5.loc[df_5["Centro_X"] <= 1150]
df_5 = df_5.loc[df_5["Centro_Y"] <= 600]
df_5 = df_5.loc[df_5["Confiança"] > 0.7]

df_6 = df_6.loc[df_6["Centro_X"] >= 800]
df_6 = df_6.loc[df_6["Centro_X"] <= 1150]
df_6 = df_6.loc[df_6["Centro_Y"] <= 600]
df_6 = df_6.loc[df_6["Confiança"] > 0.7]

df_7 = df_7.loc[df_7["Centro_X"] >= 800]
df_7 = df_7.loc[df_7["Centro_X"] <= 1150]
df_7 = df_7.loc[df_7["Centro_Y"] <= 600]
df_7 = df_7.loc[df_7["Confiança"] > 0.7]

df_8 = df_8.loc[df_8["Centro_X"] >= 800]
df_8 = df_8.loc[df_8["Centro_X"] <= 1150]
df_8 = df_8.loc[df_8["Centro_Y"] <= 600]
df_8 = df_8.loc[df_8["Confiança"] > 0.7]

video_paths = [
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 1 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 2 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 3 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 4 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 5 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 6 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 7 - HD.mp4',
    r'C:\Users\PUC\Desktop\yolo\solution 7 - video 8 - HD.mp4'
]

df_list = [df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8]

#for i, (video_path, df) in enumerate(zip(video_paths, df_list), start=1):
#    output_path = f'C:\\Users\\PUC\\Desktop\\yolo\\solution 7 - trajectory_video{i}.avi'
#    gerar_video_com_rastro(video_path, df, output_path)