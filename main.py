from src.data_loader import load_data 
from src.peak_detection import detect_peaks
from src.impurity_calc import calculate_impurity
from src.report import generate_report
import matplotlib.pyplot as plt

def main(): # main function jisme hum saree steps ko call karenge
    file_path = "data/sample_hplc.csv" # data file ka path jisme time aur intensity columns hote hai

    data = load_data(file_path) # data load karte hai jisme time aur intensity columns hote hai jise hum peaks detect karne ke liye use karenge
    peaks = detect_peaks(data) # peaks detect karte hai jisme time aur intensity dono hote hai jise hum impurity calculate karne ke liye use karenge

    purity, impurity = calculate_impurity(peaks) # impurity calculate karte hai jisme purity aur impurity dono percentage me hote hai jise hum report generate karne ke liye use karenge

    generate_report(peaks, purity, impurity)

    # Extract time and intensity for plotting
    time = data["time"]
    intensity = data["intensity"]
    peak_data = peaks

    # Smooth line
    plt.plot(time, intensity, linewidth=2)

    # Peak highlight + label
    for peak in peak_data:
        t, i = peak
        plt.scatter(t, i)

    plt.xlabel("Time (min)")
    plt.ylabel("Intensity")
    plt.title("HPLC Chromatogram")
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()