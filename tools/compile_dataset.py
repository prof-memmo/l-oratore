import json
import os
import sys

def compile_dataset():
    consegne_path = "data/consegne.json"
    cards_data_path = "js/cards-data.js"
    
    with open(consegne_path, "r", encoding="utf-8") as f:
        master_data = json.load(f)
        
    # 1. Preserve accoglienza cards
    acc_cards = [c for c in master_data["carte"] if c["mazzo"] == "accoglienza"]
    print(f"Preserving {len(acc_cards)} accoglienza cards.")
    assert len(acc_cards) == 120, "Accoglienza must have exactly 120 cards"
    
    # 2. Load the 11 generated decks
    decks_to_load = [
        "emozioni",
        "diritti",
        "digitale",
        "clima",
        "dilemmi",
        "mistero",
        "epica",
        "favole",
        "storia",
        "avventura",
        "filosofia"
    ]
    
    all_new_cards = []
    
    for deck in decks_to_load:
        module_name = f"tools.decks.{deck}"
        mod = __import__(module_name, fromlist=["CARDS"])
        deck_cards_dict = mod.CARDS
        
        deck_card_count = 0
        for lvl in ["a1", "a2", "b1", "b2", "c1", "c2"]:
            cards_list = deck_cards_dict.get(lvl, [])
            assert len(cards_list) == 20, f"Deck {deck} level {lvl} must have 20 cards, got {len(cards_list)}"
            for slot_idx, card_tuple in enumerate(cards_list, start=1):
                titolo, incipit, proibite, usare = card_tuple
                
                # validations
                assert len(proibite) == 5, f"Proibite error in {deck}_{lvl}_{slot_idx:02d}: {proibite}"
                assert len(usare) == 5, f"Usare error in {deck}_{lvl}_{slot_idx:02d}: {usare}"
                
                card_obj = {
                    "id": f"{deck}_{lvl}_{slot_idx:02d}",
                    "mazzo": deck,
                    "livello": lvl,
                    "slot": slot_idx,
                    "titolo": titolo.strip(),
                    "incipit": incipit.strip(),
                    "parole_proibite": [p.strip() for p in proibite],
                    "parole_da_usare": [u.strip() for u in usare]
                }
                all_new_cards.append(card_obj)
                deck_card_count += 1
                
        print(f"Loaded deck {deck}: {deck_card_count} cards.")
        
    assert len(all_new_cards) == 1320, f"Expected 1320 new cards, got {len(all_new_cards)}"
    
    # 3. Combine cards (keep same deck order as master_data['mazzi'])
    mazzi_order = [m["id"] for m in master_data["mazzi"]]
    print(f"Mazzi order: {mazzi_order}")
    
    cards_by_mazzo = {"accoglienza": acc_cards}
    for c in all_new_cards:
        cards_by_mazzo.setdefault(c["mazzo"], []).append(c)
        
    final_cards = []
    for m in mazzi_order:
        m_cards = cards_by_mazzo.get(m, [])
        assert len(m_cards) == 120, f"Mazzo {m} has {len(m_cards)} cards, expected 120"
        final_cards.extend(m_cards)
        
    assert len(final_cards) == 1440, f"Total cards must be 1440, got {len(final_cards)}"
    
    # 4. Global dataset validations
    all_incipits = [c["incipit"] for c in final_cards]
    all_titoli = [c["titolo"] for c in final_cards]
    
    unique_incipits = set(all_incipits)
    unique_titoli = set(all_titoli)
    
    print(f"Total cards: {len(final_cards)}")
    print(f"Unique incipits: {len(unique_incipits)} / {len(final_cards)} ({len(unique_incipits)/len(final_cards)*100:.2f}%)")
    print(f"Unique titoli: {len(unique_titoli)} / {len(final_cards)} ({len(unique_titoli)/len(final_cards)*100:.2f}%)")
    
    assert len(unique_incipits) == 1440, f"Expected 1440 unique incipits, got {len(unique_incipits)}"
    assert len(unique_titoli) == 1440, f"Expected 1440 unique titoli, got {len(unique_titoli)}"
    
    suspicious_patterns = [
        "dimostrando strutturando",
        "Sfida 0",
        "Traccia 0",
        "TODO",
        "Lorem ipsum",
        "testo da inserire"
    ]
    for c in final_cards:
        text = c["incipit"] + " " + c["titolo"]
        for p in suspicious_patterns:
            assert p not in text, f"Found suspicious pattern '{p}' in card {c['id']}: {text}"
            
    print("ALL VALIDATION CHECKS PASSED WITH 100% UNIQUENESS!")
    
    # 5. Write to data/consegne.json
    master_data["carte"] = final_cards
    master_data["totale_carte"] = 1440
    master_data["versione"] = "4.1.0"
    master_data["data_aggiornamento"] = "2026-10-23"
    
    with open(consegne_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, indent=2, ensure_ascii=False)
    print(f"Updated {consegne_path}")
    
    # 6. Write to js/cards-data.js
    with open(cards_data_path, "w", encoding="utf-8") as f:
        f.write("window.L_ORATORE_DEFAULT_CARDS = ")
        json.dump(master_data, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Updated {cards_data_path}")
    
    print("\nDataset compilation successfully completed!")

if __name__ == "__main__":
    compile_dataset()
