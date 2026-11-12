import { PRODUCT_NAME } from "@tagkin/shared";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

// Placeholder until M3 (app shell). Proves the workspace wiring.
export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{PRODUCT_NAME}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center" },
  title: { fontSize: 28, fontWeight: "700" },
});
